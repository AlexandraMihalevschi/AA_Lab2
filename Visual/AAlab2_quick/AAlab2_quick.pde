int[] numArray;
int amount = 100;
boolean sorting = false;
int operationCount = 0; // Count sorting operations
String[] buttonLabels = {"Ordered Numbers", "Random Numbers", "Reversed Numbers"};
Button[] buttons;

// QuickSort State Variables
ArrayList<int[]> stack = new ArrayList<>(); // Stores [low, high] subarrays to sort
int low = 0, high = 0, pivotIndex = -1, i = -1, j = -1;
boolean partitioning = false; // Indicates if partition step is running

void setup() {
  size(700, 700);
  numArray = new int[amount];
  buttons = new Button[3];

  for (int i = 0; i < 3; i++) {
    buttons[i] = new Button(20, 20 + i * 50, 180, 40, buttonLabels[i]);
  }

  generateRandomNumbers();
  frameRate(30); // Slow animation
}

void draw() {
  background(0);

  for (Button b : buttons) {
    b.display();
  }

  fill(255);
  textSize(16);
  textAlign(LEFT, TOP);
  text("Operations: " + operationCount, 20, height - 40);

  drawBars();

  if (sorting) {
    quickSortStep();
  }
}

void drawBars() {
  float barWidth = (width - 50) / (float) amount;
  for (int k = 0; k < amount; k++) {
    if (sorting) {
      if (k == pivotIndex) {
        fill(255, 165, 0); // Pivot (Orange)
      } else if (k == i || k == j) {
        fill(255, 0, 0); // Currently being compared (Red)
      } else if (k <= i) {
        fill(0, 255, 0); // Swapped items (Green)
      } else {
        fill(0, 150, 255); // Default (Unsorted)
      }
    } else {
      fill(0, 150, 255); // Default state
    }

    float x = 40 + k * barWidth;
    float h = constrain(numArray[k], 20, height - 100);
    rect(x, height - h - 50, barWidth - 2, h);

    fill(255);
    textAlign(CENTER, CENTER);
    textSize(16);
    text(numArray[k], x + barWidth / 2, height - h - 70);
  }
}


void quickSortStep() {
  if (!partitioning) {
    if (stack.size() > 0) {
      int[] range = stack.remove(stack.size() - 1);
      low = range[0];
      high = range[1];
      
      if (low < high) {
        pivotIndex = high;
        i = low - 1;
        j = low;
        partitioning = true;
      }
    } else {
      sorting = false;
    }
  } else {
    if (j < high) {
      operationCount++;
      if (numArray[j] < numArray[pivotIndex]) {
        i++;
        swap(i, j);
      }
      j++;
    } else {
      i++;
      swap(i, pivotIndex);
      stack.add(new int[]{low, i - 1});
      stack.add(new int[]{i + 1, high});
      partitioning = false;
    }
  }
}

void swap(int a, int b) {
  int temp = numArray[a];
  numArray[a] = numArray[b];
  numArray[b] = temp;
}

void mousePressed() {
  for (int i = 0; i < buttons.length; i++) {
    if (buttons[i].isClicked(mouseX, mouseY)) {
      sorting = false;
      operationCount = 0;
      stack.clear();

      if (i == 0) generateOrderedNumbers();
      if (i == 1) generateRandomNumbers();
      if (i == 2) generateReversedNumbers();

      stack.add(new int[]{0, amount - 1}); // Start sorting
      sorting = true;
      partitioning = false;
    }
  }
}

void generateOrderedNumbers() {
  for (int i = 0; i < amount; i++) {
    numArray[i] = int(map(i, 0, amount - 1, 20, height - 100));
  }
}

void generateRandomNumbers() {
  for (int i = 0; i < amount; i++) {
    numArray[i] = int(random(20, height - 100));
  }
}

void generateReversedNumbers() {
  for (int i = 0; i < amount; i++) {
    numArray[i] = int(map(i, 0, amount - 1, height - 100, 20));
  }
}

class Button {
  float x, y, w, h;
  String label;

  Button(float x, float y, float w, float h, String label) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.label = label;
  }

  void display() {
    fill(100, 100, 250);
    stroke(255);
    strokeWeight(2);
    rect(x, y, w, h, 10);
    fill(255);
    textAlign(CENTER, CENTER);
    textSize(16);
    text(label, x + w / 2, y + h / 2);
  }

  boolean isClicked(float mx, float my) {
    return mx > x && mx < x + w && my > y && my < y + h;
  }
}
