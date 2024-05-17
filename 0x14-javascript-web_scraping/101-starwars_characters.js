#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function getCharacters() {
  try {
    const response = await new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) reject(error);
        else resolve(JSON.parse(body));
      });
    });

    const characters = response.characters;
    for (const character of characters) {
      const characterResponse = await new Promise((resolve, reject) => {
        request.get(character, (error, response, body) => {
          if (error) reject(error);
          else resolve(JSON.parse(body).name);
        });
      });
      console.log(characterResponse);
    }
  } catch (error) {
    console.log(error);
  }
}

getCharacters();
