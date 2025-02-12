from fasthtml.common import *
from monsterui.all import *
from fasthtml.svg import *
from starlette.staticfiles import StaticFiles
from blog_index import blog_posts, BlogPostItem

app, rt = fast_app(hdrs=Theme.blue.headers())

app.mount('/markdown', StaticFiles(directory='markdown'), name='markdown')

# Define sidebar links with their respective routes
sidebar_group1 = (
    ('home', 'Posts', '/posts'),
    ('arrow-up-right', 'About', '/about'),
)

def MailSbLi(icon, title, cnt):
    return Li(A(DivLAligned(Span(UkIcon(icon)), Span(title)),
                hx_get=cnt,
                hx_target="#main-content",
                hx_swap="innerHTML",
                cls='hover:bg-secondary p-4'))

sidebar = NavContainer(
    NavHeaderLi(H3("Memoirs of the Information Age"), cls='p-3'),
    *[MailSbLi(i, t, c) for i, t, c in sidebar_group1],
    cls='mt-3'
)


@rt("/")
def index():
    return Title("Memoirs of The Information Age"), Container(
        Grid(
            Div(sidebar, cls='col-span-1'),
            Div(
                Div(
                    H3('Recent Posts'),
                    *[Li(A(BlogPostItem(post), 
                          hx_get=f"/post/{post.title.lower().replace(' ', '_')}",  # Generate URL from title
                          hx_target="#main-content",
                          hx_swap="innerHTML"), cls="list-none") for post in blog_posts],
                    cls='space-y-4 p-4'
                ),
                id="main-content",
                cls='col-span-3'
            ),
            cols_sm=1, cols_md=1, cols_lg=4, cols_xl=4,
            gap=0, cls='flex-1'
        ),
        cls=('flex', ContainerT.xl)
    )

@rt("/posts")
def posts():
    return Div(
        H3('Recent Posts'),
        *[Li(A(BlogPostItem(post),
              hx_get=f"/post/{post.title.lower().replace(' ', '_')}",
              hx_target="#main-content",
              hx_swap="innerHTML"), cls="list-none") for post in blog_posts],
        cls='space-y-4 mt-4'
    )

@rt("/about")
def about():
        # Render the Markdown content for the Home page
    with open("markdown/home_content.md", "r") as f:
        home_content_md = f.read()
        home_content = render_md(home_content_md)
    return home_content

# Route for individual blog posts
@rt("/post/{post_name}")
def post_content(request):
    post_name = request.path_params["post_name"]
    post = next((p for p in blog_posts if p.title.lower().replace(' ', '_') == post_name), None)
    if post:
        with open(post.content_path, "r") as f:
            md_content = f.read()
            return render_md(md_content)
    else:
        return H1("Post not found!")

serve()