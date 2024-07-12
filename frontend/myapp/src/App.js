import React from "react";
import axios from "axios";
import "./App.css";

class App extends React.Component {
  state = {
    movies: []
  };

  componentDidMount() {
    this.getMovies();
  }
  getMovies() {
    axios
      .get("http://127.0.0.1:8000/movieapi/")
      .then((res) => {
        this.setState({ movies: res.data });
      })
      .catch((error) => {
        console.log(error);
      });
  }
  render() {
    return (
      <div className="App">
        {this.state.movies.map((movie) => (
          <div key={movie.id}>
            <h1>{movie.name}</h1>
            <img src={movie.image} alt={movie.name} />
            <p>{movie.description}</p>
            <p>Rating: {movie.rating}</p>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
