import config
import steam_api
def main():
    
    if not config.check_project_structure():
        print("ERROR: essential files not found")
        return
    
    steam_cred, google_creed  = config.load_credentials()
    print(f"steam:{steam_cred}. | google:{google_creed}")

    steam_api.get_steam_library(steam_cred["steam_api_key"], steam_cred["steam_id"])

if __name__ == "__main__":
    main()