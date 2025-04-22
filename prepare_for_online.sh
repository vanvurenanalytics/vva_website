#!/bin/bash

#rm -rf build/html/sources build/html/static
#mv build/html/_sources build/html/sources
#mv build/html/_static build/html/static
#sed -e "s/_static/static/g" -e "s/_sources/sources/g" build/html/index.html > temp
#mv temp build/html/index.html

ln -s build/html/index.html home
ln -s build/html/services.html services
ln -s build/html/projects.html projects
ln -s build/html/blogs.html blogs
