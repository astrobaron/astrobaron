# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) { |repo_name| "https://github.com/#{repo_name}" }

# gem "rails"
gem "jekyll"

group :jekyll_plugins do
  gem 'jekyll-sitemap'
  gem 'jekyll-feed'
  gem 'jekyll-seo-tag'
end

gem "webrick", "~> 1.7"

gem "github-pages", group: :jekyll_plugins

# More Performance
gem 'liquid', github: 'Shopify/liquid', branch: 'master'
gem 'liquid-c', github: 'Shopify/liquid-c', branch: 'master'
