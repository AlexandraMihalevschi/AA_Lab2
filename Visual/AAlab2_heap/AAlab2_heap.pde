int[] numArray;
int amount = 100;
int currentI = 0;
int currentJ;
boolean sorting = false;
int operationCount = 0; // Count sorting operations
String[] buttonLabels = {"Ordered Numbers", "Random Numbers", "Reversed Numbers"};
Button[] buttons;

void setup() {
  size(700, 700);
  numArray = new int[amount];
  buttons = new Button[3];
  
  for (int i = 0; i < 3; i++) {
    buttons[i] = new Button(20, 20 + i * 50, 180, 40, buttonLabels[i]);
  }
  
  generateRandomNumbers();
  frameRate(10); // Slow animation
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
    heapSortStep();
  }
}

void drawBars() {
  float barWidth = (width - 50) / (float) amount;
  for (int i = 0; i < amount; i++) {
    if (sorting && (i == currentI || i == currentJ)) {
      fill(255, 0, 0);  // Color for swapping elements
    } else {
      fill(0, 150, 255);
    }
    
    float x = 40 + i * barWidth;
    float h = constrain(numArray[i], 20, height - 100);
    rect(x, height - h - 50, barWidth - 2, h);
    
    fill(255);
    textAlign(CENTER, CENTER);
    textSize(16);
    text(numArray[i], x + barWidth / 2, height - h - 70);
  }
}

void heapSortStep() {
  if (currentI == 0) {
    buildMaxHeap();  // Build the max heap initially
  }
  
  if (currentI < amount) {
    // Swap root with the last unsorted element
    swap(0, amount - currentI - 1);
    operationCount++;
    currentI++;
    
    // Re-heapify the root of the tree
    heapify(0, amount - currentI);
  } else {
    sorting = false;  // Finished sorting
  }
}

void buildMaxHeap() {
  // Build the max heap starting from the last non-leaf node
  for (int i = (amount / 2) - 1; i >= 0; i--) {
    heapify(i, amount);
  }
}

void heapify(int i, int n) {
  int left = 2 * i + 1;
  int right = 2 * i + 2;
  int largest = i;
  
  if (left < n && numArray[left] > numArray[largest]) {
    largest = left;
  }
  
  if (right < n && numArray[right] > numArray[largest]) {
    largest = right;
  }
  
  if (largest != i) {
    swap(i, largest);
    operationCount++;
    heapify(largest, n);  // Recursively heapify the affected subtree
  }
}

void swap(int i, int j) {
  int temp = numArray[i];
  numArray[i] = numArray[j];
  numArray[j] = temp;
}

void mousePressed() {
  for (int i = 0; i < buttons.length; i++) {
    if (buttons[i].isClicked(mouseX, mouseY)) {
      sorting = false;
      currentI = 0;
      operationCount = 0;
      
      if (i == 0) generateOrderedNumbers();
      if (i == 1) generateRandomNumbers();
      if (i == 2) generateReversedNumbers();
      
      sorting = true;
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
