{% extends "base.html" %}
{% load static %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'home/css/home.css' %}">
{% endblock %}

{% block page_header %}
<div class="container">
    <div class="row">
        <div class="col"></div>
    </div>
</div>
{% endblock %}
{% block content %}
<!--hero starts here-->
<section class="hero-container pt-5 mt-5" id="welcome">
    <div class="container-fluid py-5 mt-5">
        <div class="row d-flex align-items-center text-center py-3">
            <!--call to action-->
            <div class="col-8 col-md-10 col-lg-9 offset-lg-2 text-start text-md-end">
                <h1 class="text-start text-md-end py-2 py-lg-3 lh-1 my-2 pe-md-3 display-font" id="titleFont">GRART</h1>
                <h2 class="text-start text-md-end body-intro my-3 my-md-4" id="subTitle">AI ART & IMAGE GENERATOR </h2>
                    {% if request.user.is_authenticated %}
                    <a href="{% url 'add_tami' %}" class="text-start text-md-end text-center display-font display-6 me-3 ms-md-3" id="createArt"> CREATE</a>
                    {% else %}
                    <a href="{% url 'account_login' %}" class="text-start text-md-end text-center display-font display-6" id="createArt1">Login </a>
                    {% endif %}
                    <a href="{% url 'tami' %}" class="text-start text-md-end text-center display-font display-6 ps-md-5 ms-md-5" id="shopBtn">GALLERY</a>
            </div>
        </div>
        <!--./call-to-action-->
    </div>
</section>
<!--./end-hero-->

<!--About Starts Here-->
<section class="container-fluid" id="about">
    <div class="row py-3">
        <div class="col-12 mt-5">
            <div class="text-center mt-3 mt-sm-4 mt-md-5">
                <i class="fas fa-paint-roller fa-3x my-5"></i>
            </div>
            <h2 class="pb-2 text-center display-font heading-lg">About</h2>
            <div class="row d-flex align-items-center justify-content-center mx-auto px-lg-4 pt-3 text-center">
                <div class="col-12 py-3">
                    <p class="body-font mx-3 mx-md-4 mx-lg-5 px-3 px-md-5" id="about-text">
                        Grart is an online art community where you can create, share, and license your very own AI artwork and graphics! 
                        Grart's AI art generator is powered by <a class="link-font" href="https://mindsdb.com/" target="_blank">
                            <span class="mdb">MindsDB's</span> 
                        </a> <a class="link-font" href="https://openai.com/" target="_blank"> <span class="mdb">OpenAI </span></a> integration. Trained on datasets of famous artwork and artists, this program takes advantage of OpenAI's sophisticated <a class="link-font" href="https://openai.com/dall-e-2" target="_blank"><span class="mdb">DallE-2</span> </a> model, so users can create their own AI art with a few simple clicks. 
                        
                    </p>
                </div>
            </div>
        </div>
        <div class="col-12 text-center my-3 my-sm-4 py-3">
            <a href="#features" class="text-dark">
            <i class="fas fa-chevron-down fa-3x"></i>
            </a>
        </div>
    </div>
</section>
<!--./end-about-->

<!--Category Display https://codepen.io/mhhasan320/pen/BwqvLL -->
<section class="category-cta container-fluid" id="features">
    <div class="row">
        <div class="col-12 my-3">
            <div class="text-center mt-3 mt-md-4 mt-lg-5">
                <i class="fas fa-sitemap fa-3x"></i>
            </div>
            <h2 class="py-2 py-md-3 py-lg-4 text-center display-font text-light heading-lg my-3 text-dark">Features
            </h2>
        </div>
    </div>
    <div class="row d-flex text-white g-4 p-5">
        <div class="col-xs-8 col-sm-4">
            <div class="shadow-lg card h-100 overflow-hidden rounded-5 img-fluid" id="category-card1">
                <div class="card-image-overlay">
                    <h3 class="py-3 mt-5 mb-4 lh-1 fw-bold">
                        AI Art Gallery
                    </h3>
                    <a href="{% url 'tami' %}" class="stretched-link"></a>
                </div>
            </div>
        </div>
        <div class="col-xs-8 col-sm-4">
            <div class="card h-100 overflow-hidden rounded-5 img-fluid" id="category-card2">
                <div class="card-image-overlay">
                    <h3 class="py-3 mt-5 mb-4 lh-1 fw-bold"> Create AI Art</h3>
                    <a href="{% url 'add_tami' %}" class="stretched-link"></a>
                </div>
            </div>
        </div>
        <div class="col-xs-8 col-sm-4">
            <div class="card h-100 overflow-hidden rounded-5 img-fluid" id="category-card3">
                <div class="card-image-overlay">
                    <h3 class="py-3 mt-5 mb-4 lh-1 fw-bold">
                        Shop Art</h3>
                    <a href="{% url 'shop' %}" class="stretched-link"></a>
                </div>
            </div>
        </div>
    </div>
</section>

<footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4">
    <div class="col-md-4 d-flex align-items-center">
        <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
            <svg class="bi" width="30" height="24">
                <use xlink:href="#bootstrap"></use>
            </svg>
        </a>
        <span class="text-muted body-font">© 2023 Grart, Inc</span>
    </div>
    <!--Socials-->
    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex me-5">
        <li class="ms-3"><a class="text-muted" href="#"><svg class="bi" width="24" height="24">
                    <use xlink:href="#twitter"></use>
                </svg></a></li>
        <li class="ms-3"><a class="text-muted" href="#">
                <i class="fab fa-twitter"></i>
            </a></li>
        <li class="ms-3"><a class="text-muted" href="#">
                <i class="fab fa-facebook"></i>
            </a></li>
        <li class="ms-3"><a class="text-muted" href="#">
                <i class="fab fa-instagram"></i>
            </a></li>
    </ul>
</footer>
{% endblock %}

{% block postloadjs %}
{{ block.super }}
<!-- https://css-tricks.com/snippets/css/typewriter-effect/ -->
<script>
    var TxtType = function (el, toRotate, period) {
        this.toRotate = toRotate;
        this.el = el;
        this.loopNum = 0;
        this.period = parseInt(period, 10) || 2000;
        this.txt = '';
        this.tick();
        this.isDeleting = false;
    };

    TxtType.prototype.tick = function () {
        var i = this.loopNum % this.toRotate.length;
        var fullTxt = this.toRotate[i];

        if (this.isDeleting) {
            this.txt = fullTxt.substring(0, this.txt.length - 1);
        } else {
            this.txt = fullTxt.substring(0, this.txt.length + 1);
        }

        this.el.innerHTML = '<span class="wrap">' + this.txt + '</span>';

        var that = this;
        var delta = 200 - Math.random() * 100;

        if (this.isDeleting) { delta /= 2; }

        if (!this.isDeleting && this.txt === fullTxt) {
            delta = this.period;
            this.isDeleting = true;
        } else if (this.isDeleting && this.txt === '') {
            this.isDeleting = false;
            this.loopNum++;
            delta = 500;
        }

        setTimeout(function () {
            that.tick();
        }, delta);
    };

    window.onload = function () {
        var elements = document.getElementsByClassName('typewrite');
        for (var i = 0; i < elements.length; i++) {
            var toRotate = elements[i].getAttribute('data-type');
            var period = elements[i].getAttribute('data-period');
            if (toRotate) {
                new TxtType(elements[i], JSON.parse(toRotate), period);
            }
        }
        // INJECT CSS
        var css = document.createElement("style");
        css.type = "text/css";
        css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}";
        document.body.appendChild(css);
    };
</script>
{% endblock %}