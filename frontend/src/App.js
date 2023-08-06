import './App.css';
import GameEventViewer from './Components/GameEventViewer';
import EventFetcher from './Components/EventFetcher';

function App() {
  return (
    <div className="App">
      <EventFetcher />
      <GameEventViewer />
    </div>
  );
}

export default App;
