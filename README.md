# Stock App on Heroku

Stock App takes input from the user and plots closing price data for the last month, where data is accessed from [The Quandle WIKI](https://www.quandl.com/data/WIKI-Wiki-EOD-Stock-Prices).

This project uses Git, Flask, JSON, Pandas, Requests, Heroku, and Bokeh for visualization.
[Heroku app](https://lemurian.herokuapp.com) demonstrates the app usage.

## Setup and deploy
- Git clone the existing Stock App repository.
- `Procfile`, `requirements.txt`, `conda-requirements.txt`, and `runtime.txt`
  contain some default settings.
- HTML files are contained in `templates/`
- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.
- (Suggested) Use the [conda buildpack](https://github.com/kennethreitz/conda-buildpack).
  If you choose not to, put all requirements into `requirements.txt`

  `heroku config:add BUILDPACK_URL=https://github.com/kennethreitz/conda-buildpack.git`

  The advantages of conda include easier virtual environment management and fast package installation from binaries (as compared to the compilation that pip-installed packages sometimes require).
  One disadvantage is that binaries take up a lot of memory, and the slug pushed to Heroku is limited to 300 MB. Another note is that the conda buildpack is being deprecated in favor of a Docker solution.
- Deploy to Heroku: `git push heroku master`
- You should be able to see your site at `https://<app_name>.herokuapp.com`

## References
- Data Incubator [flask template repository](https://github.com/thedataincubator/flask-framework).
- Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).
- Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Flask: [This article](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off", and [this tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).
