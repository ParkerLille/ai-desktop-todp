pub mod app;
pub mod commands;
pub mod db;
pub mod desktop;
pub mod events;
pub mod platform;
pub mod plugins;
pub mod services;
pub mod shortcuts;
pub mod state;
pub mod tray;
pub mod windows;

pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .run(tauri::generate_context!())
        .expect("failed to run tauri application");
}
