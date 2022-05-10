module.exports = function(eleventyConfig) {
  return {
    dir: {
      input: "pages",
      output: "docs",
      includes: "../includes"
    }
  }
};
