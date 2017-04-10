
#include <osg/Program>

// Display red colour.
static const char shaderFragment[] =
    "void main() {                             \n"
    "  gl_FragColor = vec4(0.5, 0.3, 0.3, 1.0);\n"
    "}                                         \n";
// Pass geometry vertices to fragment shader.
static const char shaderVertex[] =
    "void main() {                                              \n"
    "    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;\n"
    "}                                                          \n";

osg::Program *createShaderProgram(
    const std::string &vertexShader,
    const std::string &fragmentShader)
{
    osg::Shader *vs = new osg::Shader(osg::Shader::VERTEX, vertexShader);
    osg::Shader *fs = new osg::Shader(osg::Shader::FRAGMENT, fragmentShader);
    osg::Program *prog = new osg::Program;
    prog->addShader(vs);
    prog->addShader(fs);
    return prog;
}

