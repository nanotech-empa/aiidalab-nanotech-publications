import ipywidgets as ipw


def get_start_widget(appbase, jupbase, notebase):
    return ipw.HTML(
        f"""
    <div align="center">
        <a href="{appbase}/publications.ipynb" target="_blank">
            <img src="https://github.com/nanotech-empa/aiidalab-nanotech-publications/blob/main/logo.png?raw=true" height="120px" width=243px">
        </a>
    </div>"""
    )
    
