from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from datetime import datetime
from .models import Post, Team, Theme, Tag, Division, Conference



# Create your views here.

# Devuelve los titulos de los posts
def index(request):
    posts = get_list_or_404(Post.objects.order_by('published_date'))
    dt = datetime.now()
    latestNews = Post.objects.all().order_by('-published_date')[:2:1]

    context ={'lista_posts':posts, 'news': latestNews, 'dt':dt}
    return render(request,'index.html', context)

# Devuelve un post entero
def postDetail(request, postTitle):
    p = get_object_or_404(Post, title=postTitle)
    postTags = p.tags.all()
    postTeams = p.teams.all()
    dt = datetime.now()
    latestNews = Post.objects.all().order_by('-published_date')[:2:1]

    context = {'post':p, 'tags':postTags, 'teams':postTeams,'news':latestNews, 'dt':dt}
    return render(request, 'postDetail.html', context)

#Devuelve los posts de un equipo
def team(request, teamName):
    teamFound = get_object_or_404(Team,name=teamName)
    posts = Post.objects.filter(teams= teamFound)
    dt = datetime.now()
    latestNews = Post.objects.all().order_by('-published_date')[:2:1]

    context = {'team':teamFound, 'lista_posts':posts, 'news':latestNews, 'dt':dt}
    return render(request, 'equipo.html', context)

#Devuelve los posts de un tag
def tag(request, tagName):
    tagFound = get_object_or_404(Tag,name=tagName)
    posts = Post.objects.filter(tags= tagFound)
    
    dt = datetime.now()
    latestNews = Post.objects.all().order_by('-published_date')[:2:1]

    context = {'tag':tagFound, 'lista_posts':posts, 'news':latestNews, 'dt':dt}
    return render(request, 'tag.html', context)

#Devuelve los posts de un tema
def theme(request, temaName):
    themeFound = get_object_or_404(Theme,name=temaName)
    posts = Post.objects.filter(theme= themeFound)

    dt = datetime.now()
    latestNews = Post.objects.all().order_by('-published_date')[:2:1]

    context = {'tema':themeFound, 'lista_posts':posts, 'news':latestNews, 'dt':dt}
    return render(request, 'tema.html', context)

#Devuelve los equipos de la NFL
def league(request):
    
    #DIVISIONES
    ne = get_object_or_404(Division, name='NFC East')
    nw = get_object_or_404(Division, name='NFC West')
    ns = get_object_or_404(Division, name='NFC South')
    nn = get_object_or_404(Division, name='NFC North')

    ae = get_object_or_404(Division, name='AFC East')
    aw = get_object_or_404(Division, name='AFC West')
    aso = get_object_or_404(Division, name='AFC South')
    an = get_object_or_404(Division, name='AFC North')
    
    #EQUIPOS
    net = get_list_or_404(Team.objects.filter(division=ne))
    nwt = get_list_or_404(Team.objects.filter(division=nw))
    nst = get_list_or_404(Team.objects.filter(division=ns))
    nnt = get_list_or_404(Team.objects.filter(division=nn))

    aet = get_list_or_404(Team.objects.filter(division=ae))
    awt = get_list_or_404(Team.objects.filter(division=aw))
    ast = get_list_or_404(Team.objects.filter(division=aso))
    ant = get_list_or_404(Team.objects.filter(division=an))
    
    #SIDEBAR
    latestNews = Post.objects.all().order_by('-published_date')[:2:1]

    dt = datetime.now()
    context = { 'net':net, 'nwt':nwt, 'nst':nst, 'nnt':nnt,
    'aet':aet, 'awt':awt, 'ast':ast, 'ant':ant, 'news':latestNews, 'dt':dt}
    return render(request, 'liga.html', context)


#Devuelve una lista con todos los temas
def temas(request):
    temas = get_list_or_404(Theme.objects.order_by('name'))
    latestNews = Post.objects.all().order_by('-published_date')[:2:1]

    dt = datetime.now()
    context = {'lista_temas':temas, 'news':latestNews, 'dt':dt}
    return render(request, 'temas.html', context)


#Devuelve una lista con todos los tags
def tags(request):
    tags = get_list_or_404(Tag.objects.order_by('name'))
    latestNews = Post.objects.all().order_by('-published_date')[:2:1]

    dt = datetime.now()
    context = {'lista_tags':tags, 'news':latestNews, 'dt':dt}
    return render(request, 'tags.html', context)