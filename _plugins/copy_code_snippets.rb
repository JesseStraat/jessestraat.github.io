require 'fileutils'

Jekyll::Hooks.register :site, :post_write do |site|
  source_dir = File.join(site.source, '_includes', 'code_snippets')
  destination_dir = File.join(site.dest, 'code_snippets')

  unless File.directory?(source_dir)
    puts "Error: Code snippets directory does not exist"
    next
  end

  FileUtils.mkdir_p(destination_dir)
  FileUtils.cp_r(Dir["#{source_dir}/*"], destination_dir)
  puts "Copied code snippets from #{source_dir} to #{destination_dir}"
end
