#!/usr/bin/perl

#
# Authentic Theme (https://github.com/authentic-theme/authentic-theme)
# Copyright Ilia Rostovtsev <programming@rostovtsev.io>
# Licensed under MIT (https://github.com/authentic-theme/authentic-theme/blob/master/LICENSE)
#
use strict;

our (%in, %text, $cwd, $path);

do("@{[miniserv::getenv('theme_root')]}/extensions/file-manager/file-manager-lib.pl");

my $path_urlized = urlize($path);

if (!$in{'name'}) {
    redirect_local(("list.cgi?path=$path_urlized&module=$in{'module'}" . extra_query()));
}

my $symlink    = "$cwd/$in{'name'}_symlink";
my $is_symlink = (-l $symlink);
if ($is_symlink || -d $symlink || -e $symlink) {
    print_error(
          (
           text('filemanager_create_object_exists',
                html_escape("$in{'name'}_symlink"),
                html_escape($path), ($is_symlink ? $text{'theme_xhred_global_symbolic'} : $text{'theme_xhred_global_target'})
           )
          ));
} else {
    symlink_file("$cwd/$in{'name'}", $symlink);
    redirect_local(("list.cgi?path=$path_urlized&module=$in{'module'}" . extra_query()));
}
