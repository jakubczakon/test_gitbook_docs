import pdoc

modules = ['neptune']  # Public submodules are auto-imported
context = pdoc.Context()

modules = [pdoc.Module(mod, context=context)
           for mod in modules]
pdoc.link_inheritance(context)

def recursive_text(mod):
    yield mod.name, mod.text()
    for submod in mod.submodules():
        yield from recursive_text(submod)

for mod in modules:
    for module_name, text in recursive_text(mod):
        print(module_name)
        print(text)
        print()