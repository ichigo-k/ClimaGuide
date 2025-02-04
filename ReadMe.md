# 🌍 ClimaGuide – AI-Powered Travel Companion  

**ClimaGuide** is an intelligent weather-based travel assistant designed for tourists. It leverages AI to analyze climate conditions in any location and suggests the best activities based on the weather. Whether it's a sunny beach day, a cool museum visit, or an evening city stroll, ClimaGuide ensures you make the most of your trip with personalized recommendations.  

---

## 🚀 Setup Instructions  

### Clone the Repository  
```sh
git clone git@github.com:ichigo-k/ClimaGuide.git
cd ClimaGuid
```

### Create a virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```


### Install Dependencies
```sh
pip install -r requirements.txt
```

## 🔑 Get API Keys  

You will need the following API keys:  

- **Gemini API Key** – for AI-powered activity suggestions  
- **OpenWeather API Key** – for real-time weather data  
- **Geocoding API Key** – for location-based recommendations  

### Create a `.env` file  
In the project directory, create a `.env` file and add:  

```ini
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
GEOCODING_API_KEY=your_geocoding_api_key
```
Refer to `.env.example` for more info


### Run Application
```sh
python main.py
```


## 🤝 Contribution  

Contributions are welcome! 🎉  

If you'd like to add new features, improve performance, or enhance the user experience, feel free to:  

1. **Fork the repository**  
2. **Create a new branch** (`feature-new-idea`)  
3. **Make your changes** and commit  
4. **Submit a pull request**  

Your ideas and improvements will help make **ClimaGuide** even better! 🚀  
