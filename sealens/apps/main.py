from __future__ import annotations

import pathlib

import natsort
import panel as pn
import panel.template

from .._common import get_template_class


def app():
    models = natsort.natsorted(pathlib.Path("data/models").glob("*/"))
    print(models)
    version = pn.widgets.Select(
        name="Model",
        options=models,
    )
    Template = get_template_class()
    page = Template(
        title="Time Series Analysis",
        sidebar=[
            version,
        ],
    )
    return page

    # template = pn.template.BootstrapTemplate(
    #     title="Time Series Analysis",
    #     sidebar=[
    #         version,
    #         show_bathy,
    #         specs_mesh,
    #         v_plot,
    #         metrics,
    #         station,
    #         quantile,
    #         show_colors,
    #     ],
    #     sidebar_width=sidebar_width,
    #     main=pn.Column(
    #         df_column,
    #         pn.Row(map_plot, scat_column),
    #         time_series_column,
    #     ),
    # )
    #
    # template.modal.append(settings.CONTENT)
    # modal_btn = pn.widgets.Button(name="More information about the metrics")
    #
    #
    # def about_callback(event):
    #     template.open_modal()
    #
    #
    # modal_btn.on_click(about_callback)
    # template.sidebar.append(modal_btn)
    #
    # template.servable()


page = app()
page.servable()


version = pn.widgets.Select(
    name="Model",
    options=[1, 2, 3],
)
version.servable()
