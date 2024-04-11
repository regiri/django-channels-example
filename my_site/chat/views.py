from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "chat/index.html"


class RoomView(generic.TemplateView):
    template_name = "chat/room.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["room_name"] = self.kwargs["room_name"]
        return context
