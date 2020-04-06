# functions for labels implementation
import matplotlib as mpl

def valid_string_list(list_strings):
    # Check if the argument is a list of strings
    return isinstance(list_strings, list) and all([isinstance(each_,str) for each_ in list_strings])


def valid_string(string_):
    return isinstance(string_, str)


def update_plot_count(data, child, fig):
    if data['labels_bool']:
        if isinstance(child, mpl.axes.Axes):
            data['labels_plot_count'] = data['labels_plot_count'] + 1
            data['labels_label_count'] = 0
            # print('Update plot')

        elif isinstance(child, (mpl.lines.Line2D)): #mpl.patches.Patch,
            data['labels_label_count'] = data['labels_label_count'] + 1
            # print('update label')

    return data


def get_label_(data, content):
    """
    Get label into cont. It also update the data_label_count
    :param data:
    :param content:
    :return:
    """

    if data['labels_bool']:
        # Getting values
        counter_subplot_ = data['labels_plot_count']
        counter_label_ = data['labels_label_count']

        str_ = f"\\label{{plot_{counter_subplot_:02d}-label_{counter_label_:02d}}}\n"
        # print(str_)

        if isinstance(content, str):
            content += str_
        elif isinstance(content, list):
            content.extend(str_)

        # Updating values
        # data['labels_label_count'] = data['labels_label_count'] + 1

    return data, content
