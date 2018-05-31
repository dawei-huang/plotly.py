import _plotly_utils.basevalidators


class ArraysrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='arraysrc', parent_name='scatter.error_y', **kwargs
    ):
        super(ArraysrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )