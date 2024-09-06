#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2]; // Get the Movie ID from command-line arguments
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make an HTTP GET request to the Star Wars API /films endpoint
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body);

  // Get the list of character URLs
  const characters = movieData.characters;

  // For each character URL, make a request and print the character name
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the character data and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
