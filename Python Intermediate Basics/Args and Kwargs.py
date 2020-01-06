#def function(asfs, *args = [], **kwargs = {}):


#args

# blog_1 = 'I am so awesome.'
# blog_2 = 'Cars are cool!'
# blog_3 = 'Aww look at my cat!!'
#
# site_title = 'My Blog'
#
# def blog_posts(title, *args):
#     print(title)
#     for post in args:
#         print(post)
#
# blog_posts(site_title, blog_1, blog_2, blog_3)

#kwargs

# site_title = 'My Blog'
#
# def blog_posts(title, *args, **kwargs):
#     print(title)
#     for arg in args:
#         print(arg)
#     for p_title, post in kwargs.items():
#         print(p_title, post)
#
# blog_posts(site_title,
#            '1', '2', '3',
#            blog_1 = 'I am so awesome.',
#            blog_2 = 'Cars are cool!',
#            blog_3 = 'Aww look at my cat!!')

import matplotlib.pyplot as plt

def graph_operation(x, y):
    print('function that graphs {} and {}'.format(str(x), str(y)))
    plt.plot(x, y)
    plt.show()

x1 = [1, 2, 3]
y1 = [2, 3, 1]

graph_me = [x1, y1]

graph_operation(*graph_me)