[:posts, :pages].each do |hook|
    Jekyll::Hooks.register hook, :post_render do |item|
      if item.output_ext == ".html"
        content = item.output
        # Wrap <table> tags with a div with style="overflow-x:auto;"
        content.gsub!(/<table(.*?)>/m, '<div style="overflow-x:auto;"><table\1 style="margin: 0px auto;">')
        content.gsub!(/<\/table>/m, '</table></div>')
        # Update the item content
        item.output = content
      end
    end
  end