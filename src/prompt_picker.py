from src.prompt_nu import get_prompt_nu


def prompt_picker(args):
    prompts = {
        "nu": get_prompt_nu(args),
    }
    print(f"💬 get prompt for {args.bank}")
    return prompts.get(args.bank)
