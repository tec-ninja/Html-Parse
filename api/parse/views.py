from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from bs4 import BeautifulSoup


@api_view(["POST"])
@permission_classes((AllowAny,)) 
def get_repeated_elements(request):
    html = request.data['html'].replace('\n', '')
    soup = BeautifulSoup(html, "html.parser")
    all_tags = [str(tag) for tag in soup.find_all()]
    tag_dicts = {}
    for tag in all_tags:
        if tag in tag_dicts:
            tag_dicts[tag] += 1
        else:
            tag_dicts[tag] = 1
    repeated_tags = []
    for key in tag_dicts:
        if tag_dicts[key] > 1:
            idx = key.index('>') if (key.index(' ') > key.index('>')) else key.index(' ')
            repeated_tags.append({
                'html': key,
                'count': tag_dicts[key],
                'tag': key[1:idx]
            })
    index = 0
    while index != len(repeated_tags):
        print('rrrrrrrrrr', repeated_tags, index)
        should_remove = False
        for i in range(len(repeated_tags)):
            if index != i and repeated_tags[index]['html'] in repeated_tags[i]['html']:
                should_remove = True
                break
        if (should_remove):
            repeated_tags.pop(index)
        else:
            index += 1

    return Response(repeated_tags)


