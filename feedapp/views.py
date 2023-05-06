from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from feedapp.forms import FeedCreateForm
from feedapp.models import Feed


class FeedCreateView(CreateView):
    model = Feed
    form_class = FeedCreateForm
    template_name = "feedapp/create.html"

    def form_valid(self, form):
        feed = form.save(commit=False)
        feed.writer = self.request.user
        feed.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("accountapp:detail", kwargs={"pk": self.object.writer.pk})


class FeedDetailView(DetailView):
    model = Feed
    context_object_name = "my_feed"
    template_name = "feedapp/detail.html"


class FeedEditView(UpdateView):
    model = Feed
    context_object_name = "my_feed"
    form_class = FeedCreateForm
    template_name = "feedapp/update.html"

    def get_success_url(self):
        return reverse("feedapp:detail", kwargs={"pk": self.object.pk})


class FeedDeleteView(DeleteView):
    model = Feed
    context_object_name = "my_feed"
    success_url = reverse_lazy("accountapp:index")
    template_name = "feedapp/delete.html"


class FeedListView(ListView):
    model = Feed
    context_object_name = "feed_list"
    template_name = "feedapp/list.html"
