1 Entry.objects.all()[:10]

2 Blog.objects.filter(entry__headline__contains="Lennon", entry__pub_date__year=2010)

3 SELECT * FROM posts WHERE blog = 'Technology';

4 SELECT *
  FROM your_table_name
  WHERE MONTH(date_column) = 4;

art_blog = Blog.objects.get(name='Art')
art_entries_with_comments = Entry.objects.filter(blog=art_blog,number_of_comments_gte=15)


git remote add origin https://github.com/JhoskiyCoder/Tasks.git
git branch -M main
git push -u origin maingi