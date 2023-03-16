import os
import gradio as gr
from modules import shared, script_callbacks
from psd_tools import PSDImage

value = ""
def setup_ui():
    with gr.Row().style(equal_height=False):
        with gr.Column(variant='panel'):
            # Module and model selector
            with gr.Row():
                psd_path = gr.File(file_count="multiple", file_types=[".psd"])

            with gr.Row():
                clear = gr.Button(value='Clear')
                start_train = gr.Button(value='Start Train')
            with gr.Row():
                reload = gr.Button(value='Reload UI', variant='primary')

    def fn_start_train(psd_path):
        print(psd_path[0].name)
        psd = PSDImage.open(psd_path[0].name)

        for layer in psd:
            print(layer)
            #layer.topil().save("C:\\Users\\legionfu\\Desktop\\"+layer.name+".png") #不带蒙版
            layer.compose().save("C:\\Users\\legionfu\\Desktop\\"+layer.name+".png") #带蒙版


    #psd_path.change(fn_test, inputs = psd_path, outputs = [])

    clear.click(fn_clear, inputs=psd_path)
    reload.click(fn_reload)
    start_train.click(fn_start_train, inputs=psd_path)

def fn_reload():
    pass

def fn_clear(files):
    pass

def fn_test(files):
    print(files[0])

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as auto_train_interface:
        setup_ui()

    return [(auto_train_interface, "Auto Train", "auto_train")]

script_callbacks.on_ui_tabs(on_ui_tabs)