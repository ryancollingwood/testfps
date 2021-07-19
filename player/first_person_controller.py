from ursina.entity import Entity


class FirstPersonController(Entity):

    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 5

        self.i = 0
        self.update_interval = 30

        self.cursor = Entity(
            parent = camera.ui,
            model = 'quad',
            color = color.pink,
            scale = .008,
            rotation_z = 45
            )

        self.graphics = Entity(
            name = 'player_graphics',
            parent = self,
            model = 'cube',
            origin = (0, -.5, 0),
            scale = (1, 1.8, 1),
            )

        self.position = (0, 1, 1)
        camera.rotation = (0, 0, 0)
        camera.position = (0, 1.5, 0)
        camera.fov = 90
        camera.near_clip_plane = 0.5
        mouse.locked = True

        self.smooth_camera = False
        self.rotation_speed = 1
        self.rotation_delta = 0
        self.update_rotation_x = False

        self.max_rotation_speed = 4
        self.rotation_increase_rate = 0.02

        for key, value in kwargs.items():
            setattr(self, key, value)

    def use(self):
        origin = self.world_position + self.up + (self.direction/2)
        touch_ray = raycast(origin, self.forward, ignore=[self, ], distance=2.0, debug=False)

        if touch_ray.hit:
            touch_ray.entity.push(self)

    def update(self):

        if self.i < self.update_interval:
            self.i += 1
            return

        global baddie
        baddie.rotation_y += 1
        baddie.update_facing(self.rotation)

        speed_modifier = 1

        if held_keys['left shift'] > 0:
            speed_modifier = 1.6

        rotation_delta = (held_keys['right arrow'] - held_keys['left arrow'])

        if rotation_delta == 0:
            self.rotation_speed = 0
        elif rotation_delta != self.rotation_delta:
            if rotation_delta > 0:
                self.rotation_speed = 1
            else:
                self.rotation_speed = -1

        self.rotation_delta = rotation_delta

        if self.rotation_delta == 0:
            self.rotation_speed = 0
        else:
            self.rotation_speed = lerp(self.rotation_speed, rotation_delta * self.max_rotation_speed, self.rotation_increase_rate)

        if rotation_delta == 0:
            self.rotation_y += mouse.velocity[0] * 40
        else:
            self.rotation_y += rotation_delta * abs(self.rotation_speed)

        if self.update_rotation_x:
            camera.rotation_x -= mouse.velocity[1] * 40
            camera.rotation_x = clamp(camera.rotation_x, -90, 90)

        self.y += held_keys['e'] *0.1
        self.y -= held_keys['q'] *0.1

        if held_keys["space"] > 0:
            self.use()

        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized() * speed_modifier

        if not self.smooth_camera:
            camera.position = self.position + self.up*1.5
        else:
            camera.position = lerp(
                camera.position,
                self.position + (self.up*1.5),
                time.dt * 10)

        camera.rotation_y = self.rotation_y

        origin = self.world_position + self.up + (self.direction/2)
        middle_ray = raycast(origin, self.forward, ignore=[self,], distance=1.3, debug=False)
        back_middle_ray = raycast(origin, self.back, ignore=[self, ], distance=1.3, debug=False)

        left_ray = raycast(origin, lerp(self.left, self.forward, .5), ignore=[self,], distance=1.4, debug=False)
        back_left_ray = raycast(origin, lerp(self.left, self.back, .5), ignore=[self, ], distance=1.4, debug=False)

        right_ray = raycast(origin, lerp(self.right, self.forward, .5), ignore=[self,], distance=1.4, debug=False)
        back_right_ray = raycast(origin, lerp(self.right, self.back, .5), ignore=[self, ], distance=1.4, debug=False)

        self.smooth_camera = False

        # push away from the wall
        if left_ray.hit:
            self.smooth_camera = True
            self.position -= lerp(self.left, self.forward, .5) * (1.3-left_ray.distance)
        elif back_left_ray.hit:
            self.smooth_camera = True
            self.position -= lerp(self.left, self.back, .5) * (1.3-back_left_ray.distance)
        elif back_right_ray.hit:
            self.smooth_camera = True
            self.position -= lerp(self.right, self.back, .5) * (1.3-back_right_ray.distance)
        elif right_ray.hit:
            self.smooth_camera = True
            self.position -= lerp(self.right, self.forward, .5) * (1.3-right_ray.distance)
        if not middle_ray.hit and not back_middle_ray.hit:
            self.position += self.direction * self.speed * time.dt

