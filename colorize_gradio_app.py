import gradio as gr # 引入gradio库，用于创建图形用户界面
from fastai import * # 引入fastai库，用于机器学习任务
from deoldify.visualize import * # 引入deoldify.visualize，deoldify是一个用于图片上色的库
from skimage import io # 引入skimage库，用于图片读取和保存


# 创建一个图片上色器，参数artistic=True表示使用艺术模式
colorizer = get_image_colorizer()

# 定义图片上色函数
def colorize_image(image, render_factor):
    # 创建图片路径，"input_image.jpg"是图片文件名
    image_path = "input_image.jpg"
    # 将输入的图像数组保存为RGB格式的图片
    io.imsave(image_path, image.astype('uint8'))
    # 使用上色器对图像进行上色，并展示上色结果，render_factor控制上色深度，display_render_factor=False表示不显示上色深度
    colorizer.plot_transformed_image(path=image_path, render_factor=render_factor, display_render_factor=False)
    # 返回上色后的图像路径
    return "result_images/input_image.jpg"

# 创建gradio接口，输入为图片和滑动条（控制上色深度），输出为图片，标题为"Colorizer"，描述为"Upload a black and white image and adjust the slider to colorize it."
interface = gr.Interface(
    fn=colorize_image,  # 将要运行的函数，这里是图片上色函数
    inputs=["image", gr.components.Slider(10, 40, step=1)],  # 输入参数，包括一个图片输入和一个滑动条（上色深度），滑动条的范围是10到40，步长为1
    outputs="image",  # 输出参数，是一个图片
    title="图片上色器",  # 界面的标题
    description="上传一张黑白图片并通过滑动条来进行上色。"
)

# 启动gradio接口
interface.launch()
