const {
  src, dest, watch, parallel,
} = require("gulp");
const browserify = require("browserify");
const uglify = require("gulp-uglify");
const rename = require("gulp-rename");
const sass = require("gulp-sass")(require("node-sass"));
const cleanCss = require("gulp-clean-css");
const source = require("vinyl-source-stream");
const buffer = require("vinyl-buffer");
const glob = require("glob");

const DEST_BASE = "app/static/build";
const SOURCE_BASE = "app/static/src";

function js() {
  const files = glob.sync(`${SOURCE_BASE}/js/**/*.+(js|jsx)`);
  const tasks = [];

  for (let i = 0; i < files.length; i += 1) {
    tasks.push(new Promise((resolve, reject) => {
      const entry = files[i];

      browserify({
        entries: [entry],
        extensions: [".js"],
        debug: true,
      })
        .transform("babelify", { presets: ["@babel/preset-env"] })
        .bundle()
        .pipe(source(entry.split("/").pop()))
        .pipe(buffer())
        .pipe(uglify({
          compress: true,
          mangle: { toplevel: true },
        }))
        .pipe(rename({ extname: ".min.js" }))
        .pipe(dest(`${DEST_BASE}/js`))
        .on("finish", resolve)
        .on("error", reject);
    }));
  }

  return Promise.all(tasks);
}

function scss() {
  return src([`${SOURCE_BASE}/scss/**/*.scss`])
    .pipe(sass({
      includePaths: ["node_modules"],
    }).on("error", sass.logError))
    .pipe(cleanCss())
    .pipe(rename({ extname: ".min.css" }))
    .pipe(dest(`${DEST_BASE}/css`));
}

exports.default = parallel(js, scss);

exports.watch = () => {
  watch(`${SOURCE_BASE}/scss`, scss);
  watch(`${SOURCE_BASE}/js`, js);
};

exports.build = parallel(js, scss);
