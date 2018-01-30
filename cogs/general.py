import discord
from discord.ext import commands
import config

def formatter(s):
    s = s.replace('@', '@\u200b').replace('!', '!\u200b')
    return s
def emb(text): return discord.Embed(description=text, color=config.color)

# Dont My Code
import ast, math

locals =  {key: value for (key,value) in vars(math).items() if key[0] != '_'}
locals.update({"abs": abs, "complex": complex, "min": min, "max": max, "pow": pow, "round": round})

class Visitor(ast.NodeVisitor):
    def visit(self, node):
        if not isinstance(node, self.whitelist):
            raise ValueError(node)
        return super().visit(node)

    whitelist = (ast.Module, ast.Expr, ast.Load, ast.Expression, ast.Add, ast.Sub, ast.UnaryOp, ast.Num, ast.BinOp,
            ast.Mult, ast.Div, ast.Pow, ast.BitOr, ast.BitAnd, ast.BitXor, ast.USub, ast.UAdd, ast.FloorDiv, ast.Mod,
            ast.LShift, ast.RShift, ast.Invert, ast.Call, ast.Name)

def EvalInt(expr, locals = {}):
    if any(elem in expr for elem in '\n#') : raise ValueError(expr)
    try:
        node = ast.parse(expr.strip(), mode='eval')
        Visitor().visit(node)
        return eval(compile(node, "<string>", "eval"), {'__builtins__': None}, locals)
    except Exception: raise ValueError(expr)
########

class General:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Test!')
    async def test(self):
        await self.bot.say(embed=emb(':ok_hand:'))
    @commands.command()
    async def say(self, *, say):
        await self.bot.say(embed=emb(say))
    @commands.command(description='Перевернуть слова', aliases=['r', 'rev'])
    async def reverse(self, *, text_to_reverse):
        await self.bot.say(embed=emb(text_to_reverse[::-1]))
    @commands.command(description='Калькулятор. Умножение: *, Деление: /, Плюс: +, Минус: -')
    async def calc(self, *, calc):
        await self.bot.say(embed=emb(EvalInt(calc)))
    @commands.command(pass_context=True, description='Комманда верефикации, необходима роль "Участники"')
    async def verify(self, ctx):
        for server in self.bot.servers:
            if server.name == ctx.message.server.name:
                roles = server.roles
                members = server.members
                for mem in members:
                    if mem.id == ctx.message.author.id:
                        member = mem
                        for role in roles:
                            if role.name == "Участники":
                                try:
                                    await self.bot.add_roles(member, role)
                                    await self.bot.say(embed=emb('Верификация пройдена'))
                                except: await self.bot.say(embed=emb('Нету прав давать роли'))
                                return
        await self.bot.say(embed=emb('Роль "Участники" не найдена'))

def setup(bot):
    bot.add_cog(General(bot))
