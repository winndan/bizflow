from fasthtml.common import *
from monsterui.all import *


def homepage():
    return Html(
    Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(href='https://cdn.jsdelivr.net/npm/remixicon@4.3.0/fonts/remixicon.css', rel='stylesheet'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css'),
        Link(rel='stylesheet', href='/homepage/styles.css/'),
        Title('BizFlow | Digital Builder')
    ),
    Div(
        Div(
            Span('🚀 Welcome to BizFlow! 💻'), 
            Span('🌐 Transform Your Business with 50% Off Digital Solutions! 🛠️'),
            Span('📅 Book a Free Consultation Today! 📞'),
            cls='s-banner'
        ),
        cls='s-banner-container'
    ),
    Body(
        Nav(
            Div(
                Div(
                    A(
                        Span('B'),
                        'Flow',
                        href='#'
                    ),
                    cls='nav__logo'
                ),
                Div(
                    I(cls='ri-menu-line'),
                    id='menu-btn',
                    cls='nav__menu__btn'
                ),
                cls='nav__header'
            ),
            Ul(
                Li(
                    A('About', href='#about')
                ),
                Li(
                    A('Skills', href='#skill')
                ),
                Li(
                    A('Portfolio', href='#portfolio')
                ),
                Li(
                    A('Testimonials', href='#review')
                ),
                Li(
                    A('Download CV', href='homepage/assets/CV.pdf', download='')
                ),
                id='nav-links',
                cls='nav__links'
            ),
            Div(
                A('Download CV', href='homepage/assets/CV.pdf', download=''),
                cls='nav__btn'
            )
        ),
        Header(
            Div(
                Img(src='homepage/assets/header.png', alt='header'),
                cls='header__image'
            ),
            Div(
                P('Welcome to our', cls='section__subheader'),
                H1(
                    Span('Digital Expertise'),
                ),
                P('Welcome to BizFlow!  – where small businesses get a tech-powered glow-up! 💻✨\r\n          We’re here to turn your "manual mess" into a "digital success." From sleek websites to AI wizards, We craft tools that make your business smarter, faster, and way cooler.\r\n          Let’s ditch the paperwork and embrace the future!', cls='section__description'),
                Div(
                    Button('Contact Us', cls='btn'),
                    A(
                        'Explore Products',
                        Span(
                            I(cls='ri-arrow-right-up-line')
                        ),
                        href='#'
                    ),
                    cls='header__btns'
                ),
                cls='header__content'
            ),
            id='about',
            cls='section__container header__container'
        ),
        Section(
            Div(
                H4('80+'),
                P('Satisfied clients'),
                cls='stats__card'
            ),
            Div(cls='stats__divider'),
            Div(
                H4('200+'),
                P('Project completed'),
                cls='stats__card'
            ),
            Div(cls='stats__divider'),
            Div(
                H4('99+'),
                P('Reviews given'),
                cls='stats__card'
            ),
            cls='section__container stats__container'
        ),
        Section(
            Div(
                P('Our Service', cls='section__subheader'),
                H2(
                    ' Why BizFlow? ',
                    Span('Because traditional Businesses Don’t Win.'),
                    cls='section__header'
                ),
                P('With a knack for innovation, an obsession with details, and a passion for making your life easier, \r\n          We turn your business into a modern and tech-powered. Let’s make your competitors wonder, \r\n   “How’d they do that?” ', cls='section__description'),
                Div(
                    Button('Let’s Build Something Awesome', cls='btn'),
                    cls='skill__btn'
                ),
                cls='skill__content'
            ),
            Div(
                Div(
                    Span(
                        I(cls='ri-pulse-line')
                    ),
                    H4('Websites & Apps That Don’t Just Look Good – They Work Hard.'),
                    P('Your website is your digital storefront, and We make sure it’s not just pretty but also a sales machine. From booking systems to e-commerce platforms,\r\n            We build tools that your customers will love and your business will rely on.'),
                    cls='skill__card'
                ),
                Div(
                    Span(
                        I(cls='ri-pencil-ruler-2-line')
                    ),
                    H4('Automation That Actually Works (No Robots Taking Over, Promise).'),
                    P('Tired of drowning in paperwork? Let’s automate the boring stuff so you can focus on what really matters – growing your business.\r\n            Invoices, scheduling, reminders – consider it handled.'),
                    cls='skill__card'
                ),
                Div(
                    Span(
                        I(cls='ri-graduation-cap-line')
                    ),
                    H4('AI That’s Smarter Than Your Average Bot.'),
                    P('Why settle for basic when you can have brilliant? We build AI agents that don’t just answer questions – they predict trends, engage customers, \r\n            and make your business look like a tech genius.'),
                    cls='skill__card'
                ),
                cls='skill__grid'
            ),
            id='skill',
            cls='section__container skill__container'
        ),
        Section(
            Div(
                P('Our Products', cls='section__subheader'),
                H2(
                    'Proof That We Make Effective ',
                    Span('Solutions'),
                    cls='section__header'
                ),
                P('Don’t just take my word for it – see the results! From automating a local bakery’s orders to building a booking app for a bustling salon, these projects show how I turn chaos into clarity. Spoiler:\r\n         Your business could be next.', cls='section__description'),
                Div(
                    Button('Show More', cls='btn'),
                    cls='portfolio__btn'
                ),
                cls='portfolio__content'
            ),
            Div(
                Div(
                    Img(src='homepage/assets/portfolio-1.jpg', alt='portfolio'),
                    Img(src='homepage/assets/portfolio-2.png', alt='portfolio'),
                    Img(src='homepage/assets/portfolio-3.png', alt='portfolio'),
                    Img(src='homepage/assets/portfolio-4.png', alt='portfolio'),
                    Img(src='homepage/assets/portfolio-5.png', alt='portfolio'),
                    Img(src='homepage/assets/portfolio-6.png', alt='portfolio'),
                    cls='portfolio__image'
                ),
                cls='portfolio__image__wrapper'
            ),
            id='portfolio',
            cls='portfolio__container'
        ),
        Section(
            P('Reviews', cls='section__subheader'),
            H2(
                'Our Customer Say Something',
                Span('About Us'),
                cls='section__header'
            ),
            Div(
                Div(
                    Div(
                        Div(
                            Div(
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                cls='review__ratings'
                            ),
                            P('Working with them was a game-changer. Their creative vision and\r\n                technical expertise brought our website to life, exceeding all\r\n                expectations.'),
                            Div(
                                Img(src='homepage/assets/review-1.jpg', alt='review'),
                                Div(
                                    H4('John Doe'),
                                    H5('CEO at Tech Innovations')
                                ),
                                cls='review__details'
                            ),
                            cls='review__card'
                        ),
                        cls='swiper-slide'
                    ),
                    Div(
                        Div(
                            Div(
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                cls='review__ratings'
                            ),
                            P('The project was delivered on time and within budget. Their\r\n                design skills are top-notch, and their attention to detail is\r\n                impeccable.'),
                            Div(
                                Img(src='homepage/assets/review-2.jpg', alt='review'),
                                Div(
                                    H4('Jane Smith'),
                                    H5('Manager at Creative Solutions')
                                ),
                                cls='review__details'
                            ),
                            cls='review__card'
                        ),
                        cls='swiper-slide'
                    ),
                    Div(
                        Div(
                            Div(
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                cls='review__ratings'
                            ),
                            P("I've collaborated with many web developers, but they stands out\r\n                for their exceptional creativity and professional approach."),
                            Div(
                                Img(src='homepage/assets/review-3.jpg', alt='review'),
                                Div(
                                    H4('Alice Brown'),
                                    H5('Freelance Graphic Designer')
                                ),
                                cls='review__details'
                            ),
                            cls='review__card'
                        ),
                        cls='swiper-slide'
                    ),
                    Div(
                        Div(
                            Div(
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                cls='review__ratings'
                            ),
                            P('Our new web platform is visually stunning and highly functional,\r\n                thanks to the innovative design and seamless execution.'),
                            Div(
                                Img(src='homepage/assets/review-4.jpg', alt='review'),
                                Div(
                                    H4('Robert White'),
                                    H5('Product Manager at WebCorp')
                                ),
                                cls='review__details'
                            ),
                            cls='review__card'
                        ),
                        cls='swiper-slide'
                    ),
                    Div(
                        Div(
                            Div(
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                Span(
                                    I(cls='ri-star-fill')
                                ),
                                cls='review__ratings'
                            ),
                            P('From initial concept to the final launch, they were a true\r\n                partner in creating our online presence. Their work is beautiful\r\n                and user-friendly.'),
                            Div(
                                Img(src='homepage/assets/review-5.jpg', alt='review'),
                                Div(
                                    H4('Emily Green'),
                                    H5('Entrepreneur')
                                ),
                                cls='review__details'
                            ),
                            cls='review__card'
                        ),
                        cls='swiper-slide'
                    ),
                    cls='swiper-wrapper'
                ),
                cls='swiper'
            ),
            id='review',
            cls='section__container review__container'
        ),
        Section(
            P('Contact', cls='section__subheader'),
            H2(
                "Let's Discuss Your",
                Span('Project'),
                cls='section__header'
            ),
            P("Whether you need a new website, a redesign, or custom functionality,\r\n        let's collaborate to create something amazing.", cls='section__description'),
            Form(
                Input(type='text', placeholder='Full name'),
                Input(type='text', placeholder='Your email'),
                Input(type='text', placeholder='Phone number'),
                Input(type='text', placeholder='Budget'),
                Textarea(placeholder='Message'),
                Button('Submit Message', cls='btn'),
                action='/'
            ),
            cls='section__container contact__container'
        ),
        Footer(
            P('Copyright © 2024 Web Design Mastery. All rights reserved.'),
            Ul(
                Li(
                    A(
                        I(cls='ri-facebook-fill'),
                        href='#'
                    )
                ),
                Li(
                    A(
                        I(cls='ri-twitter-fill'),
                        href='#'
                    )
                ),
                Li(
                    A(
                        I(cls='ri-linkedin-fill'),
                        href='#'
                    )
                ),
                Li(
                    A(
                        I(cls='ri-google-fill'),
                        href='#'
                    )
                ),
                cls='footer__socials'
            ),
            cls='section__container footer__container'
        ),
        Script(src='https://unpkg.com/scrollreveal'),
        Script(src='https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js'),
        Script(src='/homepage/main.js/')
    ),
    lang='en'
)