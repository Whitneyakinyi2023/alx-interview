#!/usr/bin/node

const request = require('request-promise-native'); // Use request-promise-native for Promises

// Get the movie ID from the first command-line argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as an argument');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}`;

// Function to fetch a character's name by URL
async function fetchCharacter (characterUrl) {
  try {
    const characterData = await request(characterUrl); // Fetch character data
    const character = JSON.parse(characterData); // Parse the data
    return character.name; // Return the character name
  } catch (error) {
    console.error(`Error fetching character data from ${characterUrl}:`, error);
    return null; // Return null if there's an error
  }
}

// Main function to fetch movie characters
async function fetchMovieCharacters () {
  try {
    const movieData = await request(apiUrl); // Fetch movie data
    const movie = JSON.parse(movieData); // Parse the data

    // Fetch all characters in parallel
    const characterPromises = movie.characters.map(fetchCharacter);
    const characterNames = await Promise.all(characterPromises);

    // Print each character name
    characterNames.forEach((name) => {
      if (name) console.log(name); // Only log valid names
    });
  } catch (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }
}

// Call the main function
fetchMovieCharacters();
