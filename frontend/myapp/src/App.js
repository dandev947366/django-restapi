import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

const App = () => {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getMovies = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/movieapi/");
        setMovies(response.data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    getMovies();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="App">
      {movies.map((movie) => (
        <div key={movie.id} className="movie-card">
          <h1>{movie.name}</h1>
          <img src={movie.image} alt={movie.name} />
          <p>{movie.description}</p>
          <p>Rating: {movie.rating}</p>
        </div>
      ))}
    </div>
  );
};

export default App;
