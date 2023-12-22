# Ruby

## Run older versions

Some projects might have a .ruby-version file that specifies the required Ruby version. If this file exists in your project directory, ensure its content matches the Ruby version in your Gemfile.

If you're sure that your project is compatible with Ruby e.g. "3.0.2", you can update the Ruby version specified in your Gemfile. This is a less recommended approach if you're not sure about compatibility, but it's an option:

- Open the Gemfile in your project and find the line that specifies the Ruby version, e.g., ruby `2.6.5`.
- Update it to ruby `3.0.2` and run `bundle install` to ensure all gems are compatible with the updated Ruby version.

If this doesn't work, use RVM to manage multiple Ruby versions on a single machine.

``` sh
gpg2 --keyserver hkp://keyserver.ubuntu.com --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
curl -sSL https://get.rvm.io | bash -s stable
rvm install 2.6.5
rvm use 2.6.5
```
