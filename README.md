# FB-Ad-Conversion-Prediction

## JSON sample
```
{
    "spent": 10, // float ($) 
    "age": "30-34", // str. ["30-35", "35-39", "40-44", "45-49"]
    "gender": "M", // str ["F", "M"]
    "interest1": "Travel", // str
    "interest2": "Tourism", // str
    "task": "classification", // str ["approved", "total", "classification"]
    "audience": "all" // str ["all", ""]
  }
```
## Variables
- spent: (float) add budget in dollars ($).
- age: (str) user's age.
- gender: (str) user's gender "F" for female and "M" for male.
- interest1 and interest2: (str) the list is down below.
- task: (str) ML models "approved" for regression with approved_conversion, "total" for regression with total_conversion, "classification" for classification model.
- audience: (str) if "all" predict all possible audience (age * gender = 8 combinations) if "" then return single prediction.

## Output
for "all" in audience
```
{
    "male": {
        "30-34": 0.5123357299358493,
        "35-39": 0.44840443825023735,
        "40-44": 0.4649509529631509,
        "45-49": 0.38888399096264914
    },
    "female": {
        "30-34": 0.4368318959003813,
        "35-39": 0.3797008972478586,
        "40-44": 0.3696741125022666,
        "45-49": 0.3343398492846363
    },
    "all": [
        0.5123357299358493,
        0.44840443825023735,
        0.4649509529631509,
        0.38888399096264914,
        0.4368318959003813,
        0.3797008972478586,
        0.3696741125022666,
        0.3343398492846363
    ]
}
```
for "" in audience
```
{
    "Prediction": 0.5123357299358493
}
```

## Facebook Interest list
```
facebook_interests = [
    'Current events',
    'Home and garden', 'Do it yourself (DIY)', 'Furniture', 'Gardening', 'Home Appliances',
    'Home improvement', 'Pets', 'Birds', 'Cats', 'Dogs', 'Fish', 'Horses', 'Pet food', 'Rabbits',
    'Reptiles',

    'Politics and social issues',
    'Charity and causes', 'Community issues', 'Environmentalism', 'Law', 'Military', 'Politics',
    'Religion', 'Sustainability', 'Veterans', 'Volunteering',

    'Car rentals',
    'Adventure travel', 'Tourism','Vacations', 'Travel', 'Cruises', 'Ecotourism', 'Hotels',
    'Lakes', 'Mountains', 'Nature', 'Theme parks', 'Air travel', 'Beaches',

    'Vehicles'
    'Automobiles', 'Boats', 'Electric vehicle', 'Hybrids', 'Minivans', 'Motorcycles', 'RVs', 'SUVs',
    'Scooters', 'Trucks',

    'Beauty', 'Beauty salons', 'Cosmetics', 'Fragrances', 'Hair products', 'Spas', 'Tattoos',
    'Clothing', 'Childrens clothing', 'Mens clothing', 'Shoes', 'Womens clothing', 'Fashion accessories',
    'Dresses', 'Handbags', 'Jewelry', 'Sunglasses',

    'Shopping'
    'Boutiques', 'Coupons', 'Discount stores', 'Luxury goods', 'Online shopping', 'Shopping malls',

    'Toys',

    'Boating', 'Camping', 'Fishing', 'Horseback riding', 'Hunting', 'Mountain biking', 'Surfing'

    'Sports and outdoors', 'Outdoor recreation', 'Boating', 'Camping', 'Fishing', 'Horseback riding',
    'Hunting', 'Mountain biking', 'Surfing',

    'Sports',
    'American football', 'Association football (Soccer)', 'Auto racing', 'Baseball', 'Basketball',
    'College football', 'Golf', 'Marathons', 'Skiing', 'Snowboarding', 'Swimming', 'Tennis',
    'Triathlons', 'Volleyball',

    'Computers', 'Computer memory', 'Computer monitors', 'Computer processors', 'Computer servers',
    'Desktop computers', 'Free software', 'Hard drives', 'Network storage', 'Software',
    'Tablet computers', 'Consumer electronics', 'Audio equipment', 'Camcorders', 'Cameras',
    'E-book readers', 'GPS devices', 'Game consoles', 'Mobile phones', 'Portable media players',
    'Projectors', 'Smartphones', 'Televisions'
]

```
