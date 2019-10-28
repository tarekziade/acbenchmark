module.exports = async function(context, commands) {
  let url = context.options.browsertime.url;
  await commands.navigate('https://www.example.com');
  await commands.wait.byTime(30000);
  await commands.navigate('about:blank');
  return commands.measure.start(url);
};
