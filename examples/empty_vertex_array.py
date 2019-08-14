import moderngl

import _example


class Example(_example.Example):
    title = 'Empty Vertex Array'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330

                in vec2 in_vert;
                in vec3 in_color;
                out vec3 v_color;

                void main() {
                    gl_Position = vec4(in_vert, 0.0, 1.0);
                    v_color = in_color;
                }
            ''',
            fragment_shader='''
                #version 330

                in vec3 v_color;
                out vec4 f_color;

                void main() {
                    f_color = vec4(v_color, 1.0);
                }
            ''',
        )

        vertex_data = moderngl.pack([
            0.0, 0.8, 1.0, 0.0, 0.0,
            -0.6, -0.8, 0.0, 1.0, 0.0,
            0.6, -0.8, 0.0, 0.0, 1.0,
        ])

        self.vbo = self.ctx.buffer(vertex_data)
        self.vao = self.ctx.vertex_array()

        self.vao.mode = 'TRIANGLES'
        self.vao.program = self.prog
        self.vao.bind(self.vbo.bind('in_vert', 'in_color'))
        # self.vao.bind(self.vbo.bind(0, 1, layout='2f 3f'))
        # self.vao.program = self.prog
        self.vao.vertices = 3
        self.vao.instances = 1

    def render(self, time, frame_time):
        self.ctx.screen.clear((1.0, 1.0, 1.0))
        self.vao.render()


if __name__ == '__main__':
    Example.run()