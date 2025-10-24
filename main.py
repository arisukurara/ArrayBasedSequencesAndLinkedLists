from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixConverter

def main():
    postfix = ["5 3 +",
               "8 2 - 3 +",
               "5 3 8 * +",
               "6 2 / 3 +",
               "5 8 + 3 -",
               "5 3 + 8 *",
               "8 2 3 * + 6 -",
               "5 3 8 * + 2 /",
               "8 2 + 3 6 * -",
               "5 3 + 8 2 / -"]

    print("----- Postfix Evaluator -----")
    for list in postfix:
        print(f"[{list}] = {PostfixEvaluator(list).evaluate()}")

    infix = ["A + B",
             "A + B * C",
             "( A + B ) * C",
             "A * B + C / D",
             "( A + B ) * ( C - D )",
             "A + B * C - D / E",
             "A * ( B + C ) / D",
             "( A + B * C ) / ( D - E )",
             "A +  ( B - C ) * D",
             "( A + B * ( C - D ) ) / E"]

    print("----- Infix to Postfix Converter -----")
    for list in infix:
        print(f"[{list}] = [{InfixConverter(list).convert()}]")

if __name__ == "__main__":
    main()
