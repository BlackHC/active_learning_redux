store = {}
store['timestamp']=1622112580
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=7']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=7
store['worker_id']=7
store['num_workers']=80
store['config']={'seed': 1241, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.6498241424560547})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.324516773223877})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.849571704864502})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.7473936080932617})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.9901857376098633})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 4.185880661010742})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.7801642417907715})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.3328752517700195})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 4.322925090789795})
store['active_learning_steps'][0]['training']['best_epoch']=6
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5978, 'crossentropy': 4.230361328125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.3747427463531494})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.446926236152649})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.491826057434082})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.4385781288146973})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.524900197982788})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 57640], ['ood', 37259], ['ood', 46674], ['id', 36390], ['id', 53599]], 'labels': [-1, -1, -1, 0, 8], 'scores': [1.2386568897475287, 2.1468578415574413, 2.6947351596584586, 2.9486462961108977, 3.068101134537728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.22682523727417})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.659888505935669})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.826728105545044})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.958458423614502})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.4810240268707275})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.760800361633301})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.821699619293213})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6448, 'crossentropy': 3.1041873046875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2296106815338135})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2751667499542236})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.268397569656372})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2344521284103394})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2513337135314941})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2494419813156128})
store['active_learning_steps'][1]['eval_training']['best_epoch']=5
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 7468], ['ood', 56391], ['ood', 19959], ['id', 26378], ['ood', 5394]], 'labels': [-1, -1, -1, 9, -1], 'scores': [1.229904829590439, 2.1118917747372556, 2.7481712919496397, 3.0280279451677607, 3.163751673083442]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 2.4114491939544678})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.9848852157592773})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.110452651977539})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.6862616539001465})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.76682710647583})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 4.003403663635254})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.9141764640808105})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 4.3495049476623535})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.9843430519104004})
store['active_learning_steps'][2]['training']['best_epoch']=6
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6002, 'crossentropy': 4.179026171875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.4743857383728027})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.5589501857757568})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.5422016382217407})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.5537521839141846})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.6095411777496338})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.6360535621643066})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.549037218093872})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 55207], ['ood', 32170], ['id', 45674], ['id', 19649], ['id', 19607]], 'labels': [-1, -1, 8, 9, 5], 'scores': [1.1740261953996405, 2.0431808624151504, 2.586899199364174, 2.8699833976743143, 3.016806259967119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.13154935836792})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.127041816711426})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.9886012077331543})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.7955102920532227})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.588103771209717})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 4.0450849533081055})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.761073112487793})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.9412128925323486})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 4.088824272155762})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6092, 'crossentropy': 3.9014765625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2879986763000488})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2872190475463867})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3072376251220703})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.317623257637024})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2878906726837158})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 43541], ['ood', 45144], ['ood', 32074], ['id', 55493], ['id', 5322]], 'labels': [-1, -1, -1, 2, 6], 'scores': [1.24892166479485, 2.095735921572395, 2.671029581651788, 2.97017954036816, 3.084096310426874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.0541868209838867})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.7557694911956787})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.3786044120788574})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.305608034133911})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.7168922424316406})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6212, 'crossentropy': 2.9842419921875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.4041723012924194})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.4079124927520752})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.4928314685821533})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.279855728149414})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 22960], ['ood', 55400], ['id', 18486], ['ood', 31075], ['id', 40382]], 'labels': [-1, -1, 5, -1, 5], 'scores': [1.0358704748049115, 1.7863568734461968, 2.3851012529509177, 2.770728589273592, 2.91657246561637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.18060302734375})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.7749550342559814})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.720705032348633})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.563322067260742})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.4800920486450195})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.100472450256348})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.714658260345459})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.9708306789398193})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6225, 'crossentropy': 3.83848203125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3247654438018799})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4399168491363525})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3001643419265747})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4765353202819824})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3685755729675293})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.4409130811691284})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4463237524032593})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 58999], ['ood', 28500], ['ood', 6830], ['ood', 31778], ['id', 44041]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.1004266393555207, 1.952158608152108, 2.4847047296490015, 2.7684810246057596, 2.886398053094368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.8242566585540771})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.863219976425171})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.0314016342163086})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.1583313941955566})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.282794952392578})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.345457077026367})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6249, 'crossentropy': 3.2124583984375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4349725246429443})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3228082656860352})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3691108226776123})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4265114068984985})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.3597667217254639})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 40851], ['ood', 37609], ['ood', 3738], ['ood', 34514], ['ood', 14020]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0812181693954137, 1.9719776242842908, 2.5914854732419377, 2.8832842451651306, 3.0382856513076195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.7727198600769043})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.225203514099121})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.0652120113372803})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.816638946533203})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.0203757286071777})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6303, 'crossentropy': 2.5666677734375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.244293451309204})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.2812151908874512})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.223388910293579})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1790465116500854})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 36489], ['ood', 32569], ['ood', 42365], ['id', 6759], ['id', 24815]], 'labels': [-1, -1, -1, 3, 4], 'scores': [1.072263100201233, 1.8189614854113536, 2.3745845366423914, 2.6941761242977993, 2.8740411130786168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.940779209136963})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 3.0451104640960693})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.171494483947754})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.4767255783081055})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6016, 'crossentropy': 2.03788515625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2382780313491821})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.1797194480895996})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.1761308908462524})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 36674], ['ood', 35120], ['ood', 12339], ['id', 57392], ['ood', 57020]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.0318676834958338, 1.749480467693595, 2.2739340861083344, 2.587843945432869, 2.759596664799174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.7366260290145874})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 2.5242011547088623})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.0524420738220215})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.089038610458374})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.9242427349090576})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.699293613433838})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.342461109161377})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.514364004135132})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.9622597694396973})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6018, 'crossentropy': 3.82481328125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.5836775302886963})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.4953744411468506})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.5680124759674072})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4192458391189575})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5091255903244019})
store['active_learning_steps'][9]['eval_training']['best_epoch']=2
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 22927], ['ood', 43022], ['ood', 30983], ['ood', 16351], ['id', 19254]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.286213504859436, 2.2222370447663504, 2.826723310418525, 3.055416133972173, 3.145977463546365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.8033087253570557})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.826582193374634})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.093247175216675})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.381594181060791})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.6145172119140625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 4.356290817260742})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.613, 'crossentropy': 3.309065625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.3687093257904053})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.4235098361968994})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.4359678030014038})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.417818307876587})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.4965626001358032})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 50082], ['ood', 38301], ['ood', 54058], ['id', 45029], ['ood', 42009]], 'labels': [-1, -1, -1, 5, -1], 'scores': [1.226348232294971, 2.047996436282558, 2.6197011044519156, 2.8684831618468873, 2.9650189725271634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.781816840171814})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.4196505546569824})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.442535400390625})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.52475643157959})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.8681576251983643})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.383071184158325})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.581740617752075})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 4.348864555358887})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 4.242103576660156})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 4.273237228393555})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.605, 'crossentropy': 3.97737265625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.457188367843628})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.58042573928833})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.570378303527832})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.5083143711090088})
store['active_learning_steps'][11]['eval_training']['best_epoch']=1
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 27962], ['ood', 14281], ['ood', 20967], ['id', 38446], ['ood', 31760]], 'labels': [-1, -1, -1, 0, -1], 'scores': [1.1497602104667892, 1.978835525446983, 2.5284750496715214, 2.7721488818574853, 2.8868989439682107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 1.8386027812957764})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.473431348800659})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.137697458267212})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.018568515777588})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.308537006378174})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.54093337059021})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.250302314758301})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.762155055999756})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6132, 'crossentropy': 3.587132421875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4253435134887695})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.5141406059265137})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.481305718421936})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.4481713771820068})
store['active_learning_steps'][12]['eval_training']['best_epoch']=1
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 42756], ['ood', 10000], ['ood', 108], ['ood', 20854], ['id', 26945]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.098813054279118, 1.9899260637747211, 2.5842002397704222, 2.7972032441770107, 2.8758583573179815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.7745853662490845})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.4514713287353516})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.8562560081481934})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.146933078765869})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9819726943969727})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 4.009066581726074})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.5949325561523438})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 4.053105354309082})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6227, 'crossentropy': 3.47075546875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.5401721000671387})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4500821828842163})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.380820870399475})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.4806673526763916})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.5725544691085815})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3761897087097168})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.459879755973816})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 45210], ['ood', 28713], ['ood', 19931], ['id', 38840], ['id', 13995]], 'labels': [-1, -1, -1, 9, 2], 'scores': [1.133706072520456, 2.01793393345978, 2.5399327081270515, 2.8090686985862057, 2.9360556250599377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.9686223268508911})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.9418628215789795})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.017244338989258})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.434774875640869})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.8132410049438477})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.624762773513794})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.868557929992676})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.9958910942077637})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 4.6266303062438965})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.401174545288086})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.7445573806762695})
store['active_learning_steps'][14]['training']['best_epoch']=8
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6129, 'crossentropy': 4.202650390625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.4444079399108887})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.387791633605957})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.480783462524414})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4616780281066895})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.4153048992156982})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4654783010482788})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.465808629989624})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 43112], ['ood', 27609], ['id', 253], ['ood', 8350], ['ood', 31727]], 'labels': [-1, -1, 2, -1, -1], 'scores': [1.0869638334939915, 1.955650159449509, 2.5522288035189353, 2.8598629860567435, 2.984329365508766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.877166509628296})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6192574501037598})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9402689933776855})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.1105258464813232})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.811127185821533})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.8291149139404297})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.7743515968322754})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.6607766151428223})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6314, 'crossentropy': 3.89568828125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5600517988204956})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.64500892162323})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5844926834106445})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5584286451339722})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5972552299499512})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.8113751411437988})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.5864530801773071})
store['active_learning_steps'][15]['eval_training']['best_epoch']=7
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 18405], ['ood', 3872], ['ood', 31414], ['ood', 34514], ['id', 16396]], 'labels': [-1, -1, -1, -1, 7], 'scores': [1.166516552392699, 2.047119190326078, 2.578378378421178, 2.8655344223129795, 2.987527012348524]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.948959469795227})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.6792736053466797})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.3928909301757812})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.926145076751709})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.5892, 'crossentropy': 1.9995052734375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.228861927986145})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2276887893676758})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.176314353942871})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 24589], ['ood', 49889], ['ood', 31778], ['id', 8455], ['id', 10350]], 'labels': [-1, -1, -1, 0, 5], 'scores': [0.7921278401663714, 1.4564370945756737, 1.962538365538924, 2.296021080196084, 2.5191852615502075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.969257116317749})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.713402271270752})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0616610050201416})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.181964874267578})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.1985740661621094})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6236, 'crossentropy': 2.94921796875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.4939813613891602})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.3609687089920044})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.3699619770050049})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.3445677757263184})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 9357], ['ood', 12679], ['id', 55394], ['id', 53130], ['id', 38974]], 'labels': [-1, -1, 0, 7, 8], 'scores': [1.149751860377001, 1.8878319399819423, 2.414593170515354, 2.703771867207867, 2.8631622480981607]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.663919448852539})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.4679741859436035})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.733060359954834})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.197438955307007})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.7139759063720703})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.2418630123138428})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.087761878967285})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.9725186824798584})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 4.5288801193237305})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 4.250944137573242})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6358, 'crossentropy': 3.427016796875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.4243412017822266})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.378258228302002})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.4279704093933105})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.292231559753418})
store['active_learning_steps'][18]['eval_training']['best_epoch']=1
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 44414], ['ood', 22041], ['ood', 10], ['ood', 13659], ['id', 47086]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.096819307609882, 1.9995371382802727, 2.605619165437454, 2.973892189765971, 3.1203807487876967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5665392875671387})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4354777336120605})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.2544589042663574})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.2091779708862305})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.6469497680664062})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 3.325911045074463})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 4.01616096496582})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.5500316619873047})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 3.850512981414795})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6408, 'crossentropy': 3.5466671875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3063137531280518})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3341190814971924})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3411598205566406})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4041531085968018})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.3432915210723877})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.3308892250061035})
store['active_learning_steps'][19]['eval_training']['best_epoch']=3
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 44842], ['ood', 29893], ['ood', 45181], ['id', 5258], ['ood', 43504]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.1541578280077418, 1.9764819142578172, 2.521459306592048, 2.7726550655354263, 2.878698657564743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5220690965652466})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.2314300537109375})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.7474069595336914})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.049586772918701})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.1749141216278076})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.4870104789733887})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.793771982192993})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.9207005500793457})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.8007168769836426})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6226, 'crossentropy': 3.964748828125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3478947877883911})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4823098182678223})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.4693326950073242})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3584648370742798})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4687572717666626})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 41962], ['ood', 18535], ['ood', 18279], ['id', 55415], ['id', 24024]], 'labels': [-1, -1, -1, 5, 1], 'scores': [1.1591552620544796, 1.9881214100313889, 2.5106608954222347, 2.754033938415585, 2.8758429393459073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.651684284210205})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.3789305686950684})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.644571542739868})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.023432731628418})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.3833889961242676})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6265, 'crossentropy': 2.5510451171875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.4606351852416992})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3255393505096436})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2555246353149414})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2934306859970093})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 23510], ['ood', 23124], ['ood', 29339], ['ood', 8557], ['ood', 7790]], 'labels': [1, -1, -1, -1, -1], 'scores': [0.9733374125957496, 1.76482831590759, 2.340392937537149, 2.676848611015121, 2.8550316181205453]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5090837478637695})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.4359049797058105})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.6704795360565186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.670821189880371})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.097240924835205})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.5788722038269043})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.855943202972412})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.4144692420959473})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.9836044311523438})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.924301862716675})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.6614952087402344})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6392, 'crossentropy': 3.60975}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2876496315002441})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3609216213226318})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5041885375976562})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.4154512882232666})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3701093196868896})
store['active_learning_steps'][22]['eval_training']['best_epoch']=2
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 2779], ['ood', 31437], ['ood', 10303], ['ood', 51986], ['id', 1201]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.2017292436281752, 2.069191290502916, 2.6403733594223913, 2.9360984854549317, 3.069290395274673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.5642452239990234})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.0995450019836426})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.809213638305664})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.3526864051818848})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.3537256717681885})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.475095272064209})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6331, 'crossentropy': 3.0508240234375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.3012866973876953})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3572263717651367})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.3569486141204834})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3617322444915771})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2887217998504639})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 29339], ['ood', 8611], ['ood', 50004], ['id', 28487], ['ood', 19959]], 'labels': [-1, -1, -1, 3, -1], 'scores': [1.0846573817983132, 1.9606157886650508, 2.529129105007785, 2.802732385380909, 2.9468799792787195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3185683488845825})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.1308646202087402})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.435685396194458})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8078105449676514})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6459, 'crossentropy': 1.43205263671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.111382007598877})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0459115505218506})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.0194454193115234})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 36325], ['ood', 37028], ['ood', 24855], ['ood', 13184], ['ood', 1586]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7332095287215186, 1.276927109681027, 1.713146352749094, 2.0314707418837017, 2.276114719570251]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.5481603145599365})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.320448875427246})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9222471714019775})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.2708544731140137})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6254, 'crossentropy': 1.7179681640625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.2499499320983887})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1663687229156494})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.1457945108413696})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 34784], ['ood', 13860], ['ood', 385], ['ood', 28533], ['id', 10354]], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.7804165751620369, 1.3860494861466757, 1.8270907558549547, 2.164732872733394, 2.3845274317164744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.4213619232177734})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.888806939125061})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.478101968765259})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.372084617614746})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.825316905975342})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0326485633850098})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.028749465942383})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9804306030273438})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6434, 'crossentropy': 3.0414556640625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.4071722030639648})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.420328140258789})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.319439172744751})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3700535297393799})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.4037530422210693})
store['active_learning_steps'][26]['eval_training']['best_epoch']=2
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 1389], ['ood', 35662], ['ood', 40466], ['ood', 24679], ['id', 19840]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.1794828244435875, 2.1587792435089086, 2.6994237111861246, 2.9337838436661245, 3.0281469301701724]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.4648627042770386})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.064176082611084})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.409662961959839})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.663347005844116})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6404, 'crossentropy': 1.5142693359375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.2025303840637207})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1310324668884277})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.1052000522613525})
store['active_learning_steps'][27]['eval_training']['best_epoch']=2
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 36086], ['ood', 9682], ['ood', 37418], ['ood', 37371], ['ood', 4850]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8227088004163223, 1.4991390760545826, 1.9837254376001878, 2.303945427647818, 2.5287300385511884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.4617167711257935})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.987194538116455})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.0332770347595215})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.854914665222168})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6311, 'crossentropy': 1.56764326171875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2093265056610107})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1273092031478882})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0841777324676514})
store['active_learning_steps'][28]['eval_training']['best_epoch']=3
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 38796], ['id', 51751], ['ood', 21776], ['id', 57132], ['ood', 56339]], 'labels': [-1, 1, -1, 0, -1], 'scores': [0.9045411343591456, 1.5889771284059768, 2.038995908236391, 2.3603935474506983, 2.564835770166522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.388964295387268})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.7777438163757324})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.4774768352508545})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.483774185180664})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.5980224609375})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.9460959434509277})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.652, 'crossentropy': 2.7146802734375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.218874454498291})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2557353973388672})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3019435405731201})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.315805435180664})
store['active_learning_steps'][29]['eval_training']['best_epoch']=1
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 52494], ['ood', 55194], ['ood', 25301], ['id', 987], ['ood', 29350]], 'labels': [-1, -1, -1, 6, -1], 'scores': [1.076692554023942, 1.9255402104706532, 2.425266193474166, 2.7173011808750616, 2.8703748683972146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.3346827030181885})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.9018956422805786})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.2687578201293945})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.6025378704071045})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.533029556274414})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.5296034812927246})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.762768030166626})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0942482948303223})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6567, 'crossentropy': 2.8305376953125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2121174335479736})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2355759143829346})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2744965553283691})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.311091661453247})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2931655645370483})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3185640573501587})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.308547019958496})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 37720], ['ood', 46613], ['ood', 55184], ['ood', 11821], ['ood', 24131]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.09031308094852, 1.9238057674518547, 2.4342340094670654, 2.6729259905870224, 2.791432470037668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.296708583831787})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.8229825496673584})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.9992637634277344})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.3308069705963135})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.772671699523926})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.058469295501709})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6552, 'crossentropy': 2.215008203125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1534247398376465})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2078585624694824})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.152651309967041})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1266827583312988})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.110859990119934})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 47755], ['ood', 20089], ['ood', 5553], ['ood', 8764], ['ood', 28253]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.152791680793051, 1.949802185245808, 2.458724168655815, 2.760339279771827, 2.8939731077265023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4819133281707764})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.055889129638672})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.4468839168548584})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.5965487957000732})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.945833444595337})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2339634895324707})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6533, 'crossentropy': 2.44968359375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2549362182617188})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2730185985565186})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.263249397277832})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2258155345916748})
store['active_learning_steps'][32]['eval_training']['best_epoch']=1
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 24576], ['ood', 19266], ['ood', 29255], ['ood', 19502], ['id', 2217]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.1092164799871043, 1.9316541867837906, 2.459472597820353, 2.7265241942806426, 2.8166760167094074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.3960597515106201})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.951174020767212})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.3404431343078613})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.3151237964630127})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.989438533782959})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.0216007232666016})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6602, 'crossentropy': 2.424784375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2949857711791992})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2529420852661133})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3144159317016602})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2745357751846313})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.3445045948028564})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 10303], ['ood', 9386], ['id', 52498], ['ood', 30812], ['id', 8687]], 'labels': [-1, -1, 6, -1, 9], 'scores': [1.0894212692729466, 1.8312934782246715, 2.358710848700039, 2.67930464432108, 2.8571176116925594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.470110297203064})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.685021162033081})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.1412711143493652})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4351954460144043})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.6305112838745117})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9157228469848633})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6657, 'crossentropy': 2.243577734375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2766863107681274})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2436392307281494})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2909477949142456})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.153472661972046})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1764559745788574})
store['active_learning_steps'][34]['eval_training']['best_epoch']=2
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 1266], ['ood', 21792], ['ood', 24552], ['ood', 8469], ['id', 45463]], 'labels': [-1, -1, -1, -1, 8], 'scores': [1.0206305035055414, 1.695434301844112, 2.1548837041470197, 2.447563546493729, 2.5866648627125954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4449918270111084})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.8088233470916748})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.2302985191345215})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.5033888816833496})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6642279624938965})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.655122756958008})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6458, 'crossentropy': 2.2643908203125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2189252376556396})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.174891471862793})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1985671520233154})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.241790533065796})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.244370937347412})
store['active_learning_steps'][35]['eval_training']['best_epoch']=2
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 3753], ['ood', 6323], ['ood', 59378], ['ood', 40498], ['id', 57645]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.1029161841967319, 1.9084695428772318, 2.4519674465932932, 2.7415659064126867, 2.8626525856892204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.479907512664795})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.1096787452697754})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.788888454437256})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.9542715549468994})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.1590845584869385})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.575604200363159})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6517, 'crossentropy': 2.822229296875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.344321608543396})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.3332297801971436})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3593120574951172})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3848237991333008})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3170738220214844})
store['active_learning_steps'][36]['eval_training']['best_epoch']=2
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 25297], ['ood', 45009], ['ood', 1502], ['ood', 56558], ['id', 15119]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.9960955637344409, 1.7944014061514233, 2.33237726586877, 2.6368027901799387, 2.7648409826183924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4393162727355957})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.972732424736023})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.608157157897949})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.5905561447143555})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6422, 'crossentropy': 1.561728515625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2756980657577515})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1929197311401367})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1804524660110474})
store['active_learning_steps'][37]['eval_training']['best_epoch']=3
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 25382], ['ood', 32934], ['ood', 40471], ['ood', 32574], ['ood', 4698]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8167574643554278, 1.390571157939652, 1.878180530904081, 2.213766578052824, 2.4227452593961]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.4080599546432495})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.9614274501800537})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.405933380126953})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7413384914398193})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.5720674991607666})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.653, 'crossentropy': 2.02628984375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2294788360595703})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1791040897369385})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2134385108947754})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1527470350265503})
store['active_learning_steps'][38]['eval_training']['best_epoch']=4
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 4858], ['ood', 31626], ['ood', 20485], ['ood', 22470], ['id', 11321]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.9456331934001849, 1.7247913440847853, 2.21208866010109, 2.4929818138383837, 2.659538185366152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.355668544769287})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.620303988456726})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.2868432998657227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.4391913414001465})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6513595581054688})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.4893808364868164})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.065704107284546})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.400156259536743})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.557326316833496})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.906097888946533})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.288893699645996})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.573134422302246})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.581972360610962})
store['active_learning_steps'][39]['training']['best_epoch']=10
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6593, 'crossentropy': 3.263716796875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2964890003204346})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2954539060592651})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3626303672790527})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.2675786018371582})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2492828369140625})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2778403759002686})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3373303413391113})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2702794075012207})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.3049578666687012})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 872], ['ood', 37496], ['ood', 56614], ['ood', 14237], ['id', 24968]], 'labels': [-1, -1, -1, -1, 2], 'scores': [1.0477529928834781, 1.9103954851685274, 2.5255254685019173, 2.825942327358961, 2.955166447145589]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.393099308013916})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.9532874822616577})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.088878631591797})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.378781318664551})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.793701171875})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.8601174354553223})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6537, 'crossentropy': 2.2554822265625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.238983392715454})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2185148000717163})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.2255144119262695})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2324151992797852})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1790555715560913})
store['active_learning_steps'][40]['eval_training']['best_epoch']=3
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 44496], ['ood', 34202], ['id', 3300], ['ood', 42622], ['id', 23149]], 'labels': [-1, -1, 5, -1, 4], 'scores': [1.0081753082329852, 1.7688561208262183, 2.351056106517655, 2.6684063453938496, 2.813390967461186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.393864631652832})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.675879716873169})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.986943006515503})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.319830894470215})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.7526745796203613})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.5146493911743164})
store['active_learning_steps'][41]['training']['best_epoch']=3
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6546, 'crossentropy': 2.1668111328125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2166318893432617})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1776721477508545})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.132317304611206})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.1346511840820312})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1745054721832275})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 23863], ['ood', 10319], ['ood', 30175], ['ood', 1176], ['ood', 13402]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9888259682902103, 1.8191130735954175, 2.384882069440855, 2.667507902263613, 2.78494286334345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.270337462425232})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.6285192966461182})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.1536550521850586})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.4051990509033203})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.732335090637207})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6557, 'crossentropy': 1.6556111328125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.125479817390442})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.028917670249939})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.127445936203003})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0394487380981445})
store['active_learning_steps'][42]['eval_training']['best_epoch']=2
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 20053], ['ood', 10924], ['ood', 54942], ['ood', 21776], ['ood', 16047]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0081192640195336, 1.7541042343816091, 2.2982512118675524, 2.5861634101452813, 2.723153803160617]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3561038970947266})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.6465811729431152})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.7971034049987793})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.1539461612701416})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.4234347343444824})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.583230495452881})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6679, 'crossentropy': 1.918609765625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.1599984169006348})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0761895179748535})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.0517752170562744})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0306401252746582})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.042969822883606})
store['active_learning_steps'][43]['eval_training']['best_epoch']=4
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 41468], ['ood', 23485], ['ood', 44274], ['ood', 21951], ['id', 47826]], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.9283358327212015, 1.6606524283603958, 2.1835666875531734, 2.4976363958271053, 2.645694647026649]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.287171721458435})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.5908772945404053})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.9904136657714844})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.13603138923645})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.3688466548919678})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.623300552368164})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.9437360763549805})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 3.3127660751342773})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.858825206756592})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6616, 'crossentropy': 2.7012177734375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2196564674377441})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2021100521087646})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.135606288909912})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.2539067268371582})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2456116676330566})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1858159303665161})
store['active_learning_steps'][44]['eval_training']['best_epoch']=3
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 9533], ['ood', 2548], ['ood', 23185], ['ood', 7000], ['id', 27488]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.9943373118679082, 1.875522851140683, 2.36975343991399, 2.5924793844589553, 2.706605778022623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.2703195810317993})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.651465892791748})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.09458065032959})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.5298590660095215})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.643, 'crossentropy': 1.3202154296875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.0971131324768066})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.0481081008911133})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.024552583694458})
store['active_learning_steps'][45]['eval_training']['best_epoch']=3
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 13251], ['ood', 6017], ['ood', 33064], ['ood', 45055], ['id', 17886]], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.8049273348501926, 1.331832468196477, 1.7798247131764686, 2.1093430413947507, 2.3492048554805827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.25579833984375})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.6005098819732666})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.8562257289886475})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.224907875061035})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.2610201835632324})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.486746311187744})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.978480815887451})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.905435085296631})
store['active_learning_steps'][46]['training']['best_epoch']=5
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6705, 'crossentropy': 2.4366568359375}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1512970924377441})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1288604736328125})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.072063684463501})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.103369116783142})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.150088906288147})
store['active_learning_steps'][46]['eval_training']['best_epoch']=2
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 32976], ['ood', 1010], ['id', 39279], ['ood', 7086], ['id', 1666]], 'labels': [-1, -1, 2, -1, 2], 'scores': [0.9587423614025781, 1.7504797635831428, 2.2458368853473165, 2.5223200845134848, 2.65116171136067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.394199013710022})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.584052324295044})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.013232469558716})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.2381889820098877})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.2170186042785645})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.5832395553588867})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.4940085411071777})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.670663595199585})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6801, 'crossentropy': 2.2717447265625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1549828052520752})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1593272686004639})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1826436519622803})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2936155796051025})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.174879550933838})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2332444190979004})
store['active_learning_steps'][47]['eval_training']['best_epoch']=3
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 28401], ['ood', 25350], ['ood', 6146], ['id', 9112], ['ood', 41622]], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.9092364845433256, 1.7061997937688391, 2.3197114510907975, 2.701064844254679, 2.9423556110790914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3241405487060547})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.5659533739089966})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8456242084503174})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.0434088706970215})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.246474504470825})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.24847674369812})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.357980966567993})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.467238426208496})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.764571189880371})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6796, 'crossentropy': 2.334373046875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1545071601867676})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1199626922607422})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.145782232284546})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1765183210372925})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1478180885314941})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1086888313293457})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.14510178565979})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1844067573547363})
store['active_learning_steps'][48]['eval_training']['best_epoch']=8
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 15334], ['ood', 28401], ['ood', 3612], ['ood', 14677], ['id', 5929]], 'labels': [-1, -1, -1, -1, 3], 'scores': [1.0331675760144867, 1.8713390694194705, 2.4478412507158898, 2.7395774289367276, 2.913217912291345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2463730573654175})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.7648652791976929})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.0303027629852295})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.351656436920166})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.643, 'crossentropy': 1.2847859375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.1355462074279785})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.0789510011672974})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.0548367500305176})
store['active_learning_steps'][49]['eval_training']['best_epoch']=3
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 25499], ['ood', 13401], ['ood', 29132], ['ood', 59420], ['ood', 7867]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.6391396813530994, 1.1302903924218901, 1.5298854403349385, 1.8566683739190903, 2.1123137464794652]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.2701911926269531})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4426915645599365})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.967041254043579})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.120758533477783})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.387342691421509})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.1886935234069824})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.6982598304748535})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.7692489624023438})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.855722427368164})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6673, 'crossentropy': 2.40558203125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2479277849197388})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1527433395385742})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.126219391822815})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1667473316192627})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1543984413146973})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1321465969085693})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.149714469909668})
store['active_learning_steps'][50]['eval_training']['best_epoch']=4
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 59029], ['ood', 43592], ['ood', 47409], ['ood', 7617], ['id', 38235]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.0142291556231537, 1.887617509049535, 2.409883615175425, 2.7261637143946, 2.8677769920263643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2598023414611816})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4500384330749512})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7745788097381592})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.0466692447662354})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.205988883972168})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.2975809574127197})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6901, 'crossentropy': 1.8677990234375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.0930767059326172})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.0887643098831177})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0760551691055298})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0853582620620728})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0493332147598267})
store['active_learning_steps'][51]['eval_training']['best_epoch']=5
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 2000], ['ood', 30776], ['ood', 28903], ['ood', 59399], ['id', 17156]], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.9572503996080262, 1.747626115399513, 2.3082654093004376, 2.6737438386279155, 2.842937554767433]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2787630558013916})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.4999053478240967})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7618110179901123})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.8864134550094604})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.1120805740356445})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6862, 'crossentropy': 1.4849029296875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1431689262390137})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.011406660079956})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9922052025794983})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9679398536682129})
store['active_learning_steps'][52]['eval_training']['best_epoch']=4
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 55332], ['ood', 39951], ['ood', 10690], ['ood', 11852], ['ood', 38403]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9609129606547799, 1.703418018385623, 2.188254420216494, 2.4762542610471847, 2.637532286268927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.2143290042877197})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4211690425872803})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.6814044713974})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.014681100845337})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.0710642337799072})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.7415637969970703})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6888, 'crossentropy': 1.722009375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0857361555099487})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0741240978240967})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9853360652923584})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0391911268234253})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0041284561157227})
store['active_learning_steps'][53]['eval_training']['best_epoch']=3
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 35747], ['ood', 52228], ['id', 26254], ['ood', 18855], ['id', 24433]], 'labels': [-1, -1, 1, -1, 9], 'scores': [0.8401401208743495, 1.4692502523909108, 1.9631879465836422, 2.3154289987865475, 2.5302705262659604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3263378143310547})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.514521598815918})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.9555891752243042})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.1224112510681152})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.442007064819336})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6665, 'crossentropy': 1.6134427734375}
