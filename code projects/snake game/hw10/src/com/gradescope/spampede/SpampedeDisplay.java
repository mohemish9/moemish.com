package com.gradescope.spampede;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;

/**
 * SpampedeBrain - The "View" in MVC
 * 
 * @author CS60 instructors
 */
public class SpampedeDisplay {

	/** reference to the board/spampede data being drawn */
	private SpampedeData theData;
	
	/** the display where the board is drawn */
	private Graphics theScreen;
	
	/** width of the display in pixels */
	private int width;
	
	/** height of the display in pixels */
	private int height;
	
	/** a picture of a can of spam */
	public static Image imageSpam;
	

	/** Constructor
	 * 
	 * @param theBoardInput    the data being displayed
	 * @param theScreenInput  the display to draw the board
	 * @param widthInput      width of the display (in pixels)
	 * @param heightInput     height of the display (in pixels)
	 */
	public SpampedeDisplay(SpampedeData theBoardInput, Graphics theScreenInput,
			int widthInput, int heightInput) {
		this.theScreen = theScreenInput;
		this.theData   = theBoardInput;
		this.height    = heightInput;
		this.width     = widthInput;
	}

	/* -------------------- */
	/* Displaying the board */
	/* -------------------- */
	
	/**
	 * Re-draws the board, spam, and snake (but not the buttons).
	 */
	void updateGraphics() {
		// Draw the background. DO NOT REMOVE!
		this.clear();
		
		// Draw the title
		this.displayTitle();
		
		// view the score
		this.displayScore();

		// view the # of lives
		this.displayLives();
		// Draw the board?
		
		// TODO: Add your code here :) 
		// The method drawSquare (below) will likely be helpful :) 
		int colNum = this.theData.getNumColumns();
		int rawNum = this.theData.getNumRows();
		for (int col = 0; col < colNum; col++) {
			for (int raw = 0; raw<rawNum; raw++) {
				
				BoardCell current = this.theData.getCell(raw, col);
				this.drawSquare(45 + Preferences.CELL_SIZE * col, 45 + Preferences.CELL_SIZE * raw, current.getCellColor());
			}
		}
		// Display an image, just for fun.
		if (SpampedeDisplay.imageSpam != null) {
			this.theScreen.drawImage(SpampedeDisplay.imageSpam, 200, 370, null);
		}
		
		// Draw the game-over message, if appropriate.
		if (this.theData.getGameOver()) {
			this.displayGameOver();
		}

	}

	/**
	 * Draws a cell-sized square with its upper-left corner
	 * at the given pixel coordinates (i.e., x pixels to the right and 
	 * y pixels below the upper-left corner) on the display.
	 * 
	 * @param x  x-coordinate of the square, between 0 and this.width-1 inclusive
	 * @param y  y-coordinate of the square, between 0 and this.width-1 inclusive
	 * @param cellColor  color of the square being drawn
	 */
	public void drawSquare(int x, int y, Color cellColor) {
		this.theScreen.setColor(cellColor);
		this.theScreen.fillRect(x, y, Preferences.CELL_SIZE,
				Preferences.CELL_SIZE);
	}

	/**
	 * Draws the background. DO NOT MODIFY!
	 */
	void clear() {
		this.theScreen.setColor(Preferences.COLOR_BACKGROUND);
		this.theScreen.fillRect(0, 0, this.width, this.height);
		this.theScreen.setColor(Preferences.TITLE_COLOR);
		this.theScreen.drawRect(0, 0, this.width - 1,
				Preferences.GAMEBOARDHEIGHT - 1);
	}

	/* ------------ */
	/* Text Display */
	/* ------------ */
	
	/**
	 * Displays the title of the game.
	 */
	public void displayTitle() {
		this.theScreen.setFont(Preferences.TITLE_FONT);
		this.theScreen.setColor(Preferences.TITLE_COLOR);
		this.theScreen.drawString(Preferences.TITLE, 
				Preferences.TITLE_X, Preferences.TITLE_Y);
	}

	/**
	 * Displays the score
	 */
	public void displayScore() {
		this.theScreen.setFont(Preferences.SCORE_FONT);
		this.theScreen.setColor(Preferences.SCORE_COLOR);
		this.theScreen.drawString(this.theData.getScore(), 
				Preferences.SCORE_X, Preferences.SCORE_Y);
	}
	/**
	 * Displays the # of lives
	 */
	public void displayLives() {
		this.theScreen.setFont(Preferences.LIVES_FONT);
		this.theScreen.setColor(Preferences.LIVES_COLOR);
		this.theScreen.drawString(this.theData.getLives(), 
				Preferences.LIVES_X, Preferences.LIVES_Y);
	}
	
	/**
	 * Displays the game-over message.
	 */
	public void displayGameOver() {
		this.theScreen.setFont(Preferences.GAME_OVER_FONT);
		this.theScreen.setColor(Preferences.GAME_OVER_COLOR);
		this.theScreen.drawString(Preferences.GAME_OVER_TEXT,
				Preferences.GAME_OVER_X, Preferences.GAME_OVER_Y);
	}

}
