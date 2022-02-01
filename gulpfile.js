'use strict';

const { src, dest, watch, parallel } = require('gulp');
const rename = require('gulp-rename');
const babel = require('gulp-babel');
const sourcemaps = require('gulp-sourcemaps');
const sass = require('gulp-sass')(require('node-sass'));
const cleanCss = require('gulp-clean-css');

var browserify = require('browserify');
var babelify = require('babelify');
var gulp = require('gulp');
var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');
var util = require('gulp-util');
var plumber = require('gulp-plumber');
var transform = require('vinyl-transform');
var glob = require('glob');
const es = require('event-stream');

const paths = {
  jsx: ['static_src/js/**/*.jsx'],
  scss: ['static_src/scss/**/*.scss'],
};

function scss() {
  return src(paths.scss)
    .pipe(sass({
      includePaths: ['node_modules'],
    }).on('error', sass.logError))
    .pipe(cleanCss())
    .pipe(rename({ extname: '.min.css' }))
    .pipe(dest('static_build/css'));
}

// function jsx() {
//   return src(paths.jsx)
//     .pipe(sourcemaps.init())
//     // .pipe(sass({
//     //     includePaths: ['node_modules'],
//     // }).on('error', sass.logError))
//     // .pipe(cleanCss())
//     .pipe(babel({
// 			presets: [['@babel/preset-env', {}], '@babel/preset-react'],
// 		}))
//     .pipe(rename({ extname: '.min.js' }))
// 		.pipe(dest('static_build/js'));
// }

function jsx(done) {
  const JSX_SOURCE_PATH = 'static_src/js'
  const JSX_DEST_PATH = 'static_build/js'

  const files = glob.sync(`./${JSX_SOURCE_PATH}/**/*.jsx`);
  const tasks = [];

  for (let i=0; i<files.length; ++i) {
    tasks.push(new Promise((resolve, reject) => {
      const entry = files[i];

      browserify({
        entries: [entry],
        extensions: ['.jsx'],
        debug: true,
      })
        .transform("babelify", {presets: ["@babel/preset-env", "@babel/preset-react"]})
        .bundle()
        .pipe(source(entry.split(`${JSX_SOURCE_PATH}/`).pop()))
        .pipe(rename({ extname: '.min.js' }))
        .pipe(dest(JSX_DEST_PATH))
        .on('finish', resolve)
        .on('error', reject)
    }))
  }

  return Promise.all(tasks)

  // const b = browserify({
  //   entries: glob.sync('./static_src/js/**/*.jsx'),
  //   extensions: ['.jsx'],
  //   debug: true,
  // }).transform("babelify", {presets: ["@babel/preset-env", "@babel/preset-react"]})

  // return b.bundle()
  //   .pipe(source('app.js'))
  //   .pipe(plumber())
  //   .pipe(dest('static_build/js'))
}

exports.default = parallel(scss, jsx);

exports.watch = () => {
  watch(paths.scss, scss);
  watch(paths.jsx, jsx);
};

exports.build = parallel(scss, jsx);
