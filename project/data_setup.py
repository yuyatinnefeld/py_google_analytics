data_range = None


def set_daterange(start, end):
    data_range = [{"startDate": start, "endDate": end}]
    return data_range


def set_metrics(metrics1, metrics2):
    metrics = [
        {"expression": metrics1},
        {"expression": metrics2},
    ]
    return metrics


def set_dimensions(dimension1):
    dimensions = [
        {"name": dimension1},
    ]
    return dimensions
