
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    # Obsługa filtrowania po autorze
    def get_queryset(self):
        queryset = super().get_queryset()
        author_query = self.request.GET.get('author')
        if author_query:
            queryset = queryset.filter(author__icontains=author_query)
        return queryset

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = 'books/book_form.html'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = 'books/book_form.html'

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')
    template_name = 'books/book_confirm_delete.html'