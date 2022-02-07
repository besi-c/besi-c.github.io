module.exports = function(eleventyConfig) {

  // Copy `x/` to `_site/x`
  //eleventyConfig.addPassthroughCopy("files");
  //eleventyConfig.addPassthroughCopy("images");

  // Output directory: _site
  return {
    dir: {
      input: "pages",
      output: "docs",
      includes: "../includes"
    }
  }
};
