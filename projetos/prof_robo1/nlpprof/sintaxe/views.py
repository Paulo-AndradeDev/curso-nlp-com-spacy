from django.shortcuts import render
from django.http import HttpResponse
from . import utils

def index(request):

    return HttpResponse(utils.displacy_dep("Samuel Nunes Andrade é level 5 no jogo starf Field na cidade de João Pessoa no ano de 2023"))
