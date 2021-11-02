import { render, screen } from '@testing-library/react';
import App from './App';

test('Page loading check', () => {
  render(<App />);
  const linkElement = screen.getByText(/Pokemon Search Engine/i);
  expect(linkElement).toBeInTheDocument();
});
