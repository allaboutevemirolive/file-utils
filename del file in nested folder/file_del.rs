use std::fs;
use std::path::Path;

fn delete_files_with_extension(dir: &Path, extension: &str) -> std::io::Result<()> {
    if dir.is_dir() {
        for entry in fs::read_dir(dir)? {
            let entry = entry?;
            let path = entry.path();

            if path.is_dir() {
                delete_files_with_extension(&path, extension)?;
            } else if let Some(file_name) = path.file_name() {
                if let Some(ext) = file_name.to_str().and_then(|name| name.split('.').last()) {
                    if ext == extension {
                        fs::remove_file(&path)?;
                        println!("Deleted file: {:?}", path);
                    }
                }
            }
        }
    }

    Ok(())
}

fn main() {
    let directory = std::env::current_dir().expect("Failed to get current directory");

    if let Err(err) = delete_files_with_extension(&directory, "rs") {
        eprintln!("Error deleting files: {}", err);
    }
}